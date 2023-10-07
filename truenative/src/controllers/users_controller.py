from datetime import datetime, timedelta
import random
import logging
import hashlib
import requests
import time

from utils import create_ruv, VerificationStatus, is_approved_random
from db import DatabaseClient
from models.user_verification import UserVerification
from errors import TransactionAlreadyRequested
from queue_processor import enqueue_task
from environment import get_secret_token, get_webhook_delay, get_success_rate


db = DatabaseClient("users")

def _process_task(ruv: str) -> bool:
    try:
        time.sleep(1)
        data = db.get(ruv)
        user_verification = UserVerification()
        user_verification.load(data)
        if not VerificationStatus.in_progress(user_verification.task_status):
            db.audit(ruv, "[VERIFY] Task %s was removed from the queue since status was %s" % (ruv, user_verification.task_status))
            logging.warn("[VERIFY] Status is not correct in the app, %s: %s" % (ruv, user_verification.task_status))
            # Ya fue procesada, edge case para evitar errors
            return True
        
        now = datetime.now()
        if now >= user_verification.processed_at:
            user_verification.status = "VERIFICADO" if is_approved_random(success_percentage=get_success_rate()) else "NO_VERIFICADO"
            logging.info("[VERIFY] process %s ended with status: %s" % (ruv, user_verification.status))
            # TODO Validate this code again in the next versions
            #score = calculate_score(user_verification.user)
            if user_verification.status == "VERIFICADO":
                user_verification.score = (random.random() * 40) + 60
            else:
                user_verification.score = (random.random() * 50)
            user_verification.task_status = str(VerificationStatus.PROCESSED)
            db.save(ruv, user_verification.raw())
            db.audit(ruv, "[VERIFY] Task %s was processed and the score was %s" % (ruv, user_verification.score))
            _notify(user_verification)
            return True
        else:
            # Debe ejecutarse la tarea de nuevo
            return False

    except Exception as err:
        logging.error(err, exc_info=True)
        db.audit(ruv, "[VERIFY] Task %s finished with error %s" % (ruv, str(err)))
        return True


def _notify(user_verification: UserVerification) -> None:
    try:
        webhook = user_verification.user_webhook

        result = user_verification.resp()

        for key, value in result.items():
            # Si el valor es un objeto datetime, convertirlo a cadena de texto en formato ISO 8601
            if isinstance(value, datetime):
                result[key] = value.strftime("%Y-%m-%dT%H:%M:%S")
        
        token = f"{get_secret_token()}:{user_verification.ruv}:{result['score']}"
        result["verifyToken"] = hashlib.sha256(token.encode()).hexdigest()

        response = requests.patch(webhook, json=result)
        if response.status_code == 200:
            db.audit(user_verification.ruv, "[VERIFY] Task %s result was notified to %s with status 200" % (user_verification.ruv, webhook))
            logging.info(f"[VERIFY] Successful request")
        else:
            db.audit(user_verification.ruv, "[VERIFY] Task %s result could not be notified to %s, result was %s" % (user_verification.ruv, webhook, response.status_code))
            logging.warn(f"[VERIFY] Request failed with status code {response.status_code}")
    except Exception as err:
        logging.error(err, exc_info=True)
        db.audit(user_verification.ruv, "[VERIFY] Task %s result could not be notified due to error %s" % (user_verification.ruv, err))
        logging.error("[VERIFY] Error notifying the result %s" % str(err))


def create_task(user_id: str, transaction_id: str, user: dict, user_webhook: str) -> dict:
    ruv = create_ruv(transaction_id, user_id)
    data = db.get(ruv)

    if data is not None and data["task_status"] != str(VerificationStatus.PROCESSED):
        raise TransactionAlreadyRequested()
    now = datetime.now()
    delay = random.randint(0, get_webhook_delay())
    delayed_time = now + timedelta(seconds=delay)

    verification = UserVerification()
    verification.ruv = ruv
    verification.user_id = user_id
    verification.transaction_id = transaction_id
    verification.created_at = now
    verification.processed_at = delayed_time
    verification.user = user
    verification.user_webhook = user_webhook
    verification.task_status = str(VerificationStatus.ACCEPTED)

    db.save(ruv, verification.raw())
    db.audit(ruv, "[VERIFY] Task %s was created" % (ruv))

    enqueue_task(ruv, _process_task)
    db.audit(ruv, "[VERIFY] Task %s was enqueued to be processed in %s seconds" % (ruv, delay))

    return verification.short()

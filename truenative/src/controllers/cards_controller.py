from datetime import datetime, timedelta
import random
import logging

from utils import create_ruv, create_token, VerificationStatus, is_approved_random
from models.card_verification import CardVerification
from errors import TransactionAlreadyRequested
from db import DatabaseClient
from environment import get_success_rate, get_poll_delay


db = DatabaseClient("cards")


def _get_issuer(card_number:str) -> str:
    # Eliminar espacios y guiones en el número de tarjeta
    card_number = card_number.replace(" ", "").replace("-", "")

    # Verificar el emisor basado en los primeros dígitos
    if card_number.startswith("4"):
        return "VISA"
    elif card_number.startswith(("51", "52", "53", "54", "55")):
        return "MASTERCARD"
    elif card_number.startswith("34") or card_number.startswith("37"):
        return "AMERICAN EXPRESS"
    elif card_number.startswith("6"):
        return "DISCOVER"
    elif card_number.startswith(("30", "36", "38")):
        return "DINERS CLUB"
    else:
        return "UNKNOWN"


def create_task(transaction_id: str, card: dict) -> dict:
    card_token = create_token(card)
    ruv = create_ruv(transaction_id, card_token)
    data = db.get(ruv)

    if data is not None and data["status"] != str(VerificationStatus.PROCESSED):
        raise TransactionAlreadyRequested()

    now = datetime.now()
    delay = random.randint(0, get_poll_delay())
    delayed_time = now + timedelta(seconds=delay)

    verification = CardVerification()
    verification.ruv = ruv
    verification.transaction_id = transaction_id
    verification.created_at = now
    verification.processed_at = delayed_time
    verification.card = card
    verification.token = card_token
    verification.task_status = str(VerificationStatus.ACCEPTED)
    verification.issuer = _get_issuer(card["cardNumber"])

    logging.info("[CARD] Task %s was created and will be processed in %s s" % (ruv, delay))

    db.save(ruv, verification.raw())
    db.audit(ruv,"[CARD] Task %s was created and will be processed in %s s" % (ruv, delay))

    return verification.short()


def get_task(ruv: str) -> dict:
    data = db.get(ruv)
    if not data:
        return None
    card_verification = CardVerification()
    card_verification.load(data)
    if card_verification.task_status == str(VerificationStatus.PROCESSED):
        return card_verification.resp()
    if card_verification.task_status == str(VerificationStatus.ACCEPTED):
        card_verification.task_status = str(VerificationStatus.PENDING)
        db.save(ruv, card_verification.raw())
        db.audit(ruv, "[CARD] Task %s was updated to %s" % (ruv, VerificationStatus.PENDING))
        return None
    else:
        now = datetime.now()
        if now >= card_verification.processed_at:
            status = "APROBADA" if is_approved_random(success_percentage=get_success_rate()) else "RECHAZADA"
            logging.info("[CARD] Verification %s: %s" % (ruv, status))
            card_verification.status = status
            card_verification.task_status = str(VerificationStatus.PROCESSED)
            db.save(ruv, card_verification.raw())
            db.audit(ruv, "[CARD] Task %s was processed and the result was %s" % (ruv, status))
        return None

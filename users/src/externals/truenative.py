# Importación de dependencias
from externals.models import TrueNative, UserNative
from requests.structures import CaseInsensitiveDict
import requests
import logging
import uuid
import os
import json

# Constantes
LOG = "[Verify User External]"

# Función que retorna la información del trayecto
def verifyUserExternal(userid, user, headers):
    TRUENATIVE_PATH = os.environ["TRUENATIVE_PATH"]
    USERS_PATH = os.environ["USERS_PATH"]
    SECRET_TOKEN = os.environ["SECRET_TOKEN"]
    logging.info(f"{LOG} Constantes => ")
    logging.info(f"TRUENATIVE_PATH => [{TRUENATIVE_PATH}]")
    logging.info(f"USERS_PATH => [{USERS_PATH}]")
    logging.info(f"SECRET_TOKEN => [{SECRET_TOKEN}]")  
    
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Authorization"] = f"Bearer {SECRET_TOKEN}"
    # Create user Native
    userNative = UserNative(
        email = user.get('email'),
        dni = user.get('dni'),
        fullName = user.get('fullName'),
        phone = user.get('phoneNumber')
    )
    identificador = str(uuid.uuid4())
    request = TrueNative(
        transactionIdentifier = identificador,
        userIdentifier = str(userid),
        userWebhook = f"{USERS_PATH}/users/native/callback",
        user = userNative.__dict__
    )
    
    logging.info(f"{LOG} Transaction request => ")
    logging.info(json.loads(json.dumps(request.__dict__)))
    logging.info(f"{LOG} Transaction headers => ")
    logging.info(headers)
    urlTrueNative = f"{TRUENATIVE_PATH}/native/verify"
    logging.info(f"{LOG} Transaction URI => ")
    logging.info(urlTrueNative)
    # Call true Native
    result =  requests.post(urlTrueNative, json = json.loads(json.dumps(request.__dict__)), headers=headers)
    logging.info(f"{LOG} Transaction response => [{result.status_code}]")
    logging.info(result.content)
    return result.json()

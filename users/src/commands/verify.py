# Importación de dependencias
from commands.base_command import BaseCommannd
from requests.structures import CaseInsensitiveDict
from errors.errors import ApiError
from commands.update import UpdateUser
from models.models import UserSchema
from validators.validators import validateSchema, verifyCallbackSchema
import requests
import logging
import os

# Constantes
SECRET_TOKEN = os.getenv("SECRET_TOKEN", default="d5f14860-f674-4248-be61-18bed307a49f")
SEND_EMAIL_PATH = os.getenv("SEND_EMAIL_PATH")
LOG = "[Verify User]"

# Esquemas
userSchema = UserSchema()

# Clase que contiene la logica de verificación de usuarios
class VerifyUser(BaseCommannd):
    def __init__(self, data):
        validateSchema(data, verifyCallbackSchema)
        self.data = data

    # Función que construye el request de SendEmail
    def constructRequest(self, user, truenative):
        return {
            "name": f"{user['username']}",
            "dni": f"{user['dni']}",
            "ruv": f"{truenative['RUV']}",
            "estado": f"{truenative['status']}",
            "createAt": f"{truenative['createdAt']}",
            "emailTo": f"{user['email']}"
        }

    # Función que envia el email informativo al usuario
    def sendEmail(self, user, truenative):
        logging.info(f"{LOG} SendEmail URI => ")
        logging.info(SEND_EMAIL_PATH)
        requestSendEmail = self.constructRequest(user, truenative)
        logging.info(f"{LOG} SendEmail Request => ")
        logging.info(requestSendEmail)
        headers = CaseInsensitiveDict()
        headers["secret-x"] = SECRET_TOKEN
        logging.info(f"{LOG} SendEmail Headers Request => ")
        logging.info(headers)
        # Call to Send Email Service
        responseSendEmail = requests.post(
            SEND_EMAIL_PATH, json=requestSendEmail, headers=headers)
        if responseSendEmail.status_code != 200:
            logging.error(
                f"{LOG} SendEmail Status Response => [{responseSendEmail.status_code}]")
            logging.error(responseSendEmail.content)
            raise ApiError
        logging.info(f"{LOG} SendEmail Response => ")
        logging.info(responseSendEmail.content)
        return True

    # Función que realiza la actualización del usuario
    def execute(self):
        try:
            logging.info(f"{LOG} Transaction request => ")
            logging.info(self.data)
            dataToUpdate = {"status": f"{self.data['status']}"}
            logging.info(f"{LOG} User status from TrueNative => ")
            logging.info(dataToUpdate)
            userUpdated = UpdateUser(
                self.data['userIdentifier'], dataToUpdate).execute()
            userUpdatedJson = userSchema.dump(userUpdated)
            self.sendEmail(userUpdatedJson, self.data)            
            logging.info(f"{LOG} Transaction response => ")
            logging.info(userUpdatedJson)
            return userUpdatedJson
        except Exception as e:
            logging.error(e)
            raise ApiError(e)

# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError, MissingToken, TokenInvalid
from validators.validators import validateSchema, sendMailSchema
from email.message import EmailMessage
from flask.json import jsonify
import smtplib
import logging
import os

# Constantes
SECRET_TOKEN_USER_NOT = os.getenv("SECRET_TOKEN_USER_NOT", default="d5f14860-f674-4248-be61-18bed307a49f")
SECRET_TOKEN_CARD_NOT = os.getenv("SECRET_TOKEN_CARD_NOT", default="d5f14860-f674-4248-be61-18bed307a4a0")
MAIL_ACCOUNT_USER = os.getenv("MAIL_ACCOUNT_USER", default="misopruebas@gmail.com")
MAIL_ACCOUNT_PASSWORD = os.getenv("MAIL_ACCOUNT_PASSWORD", default="jmek wgba shnf msdr")
MAIL_SUBJECT = os.getenv("MAIL_SUBJECT", default="Miso Notificaciones")
MAIL_SMTP = os.getenv("MAIL_SMTP", default="smtp.gmail.com:587")
LOG = "[Verify User]"

# Clase que contiene la logica de creción de usuarios
class SendMail(BaseCommannd):
    def __init__(self, request, headers):
        self.data = request
        self.headers = headers
        logging.info(f"{LOG} Transaction request => ")
        logging.info(self.data)
        logging.info(f"{LOG} Transaction headers request => ")
        logging.info(self.headers)
        self.validateRequest(self.data, headers)
        self.template = None
        self.dictValues = None

    # Función que valida los headers del servicio
    def validateHeaders(self, headers):
        if not "secret-x" in headers:
            logging.error(f"{LOG} Error [validateHeaders] => ")
            logging.error(MissingToken.description)
            raise MissingToken
        if headers["secret-x"] != SECRET_TOKEN_USER_NOT and headers["secret-x"] != SECRET_TOKEN_CARD_NOT:
            logging.error(f"{LOG} Error [validateHeaders] => ")
            logging.error(TokenInvalid.description)
            raise TokenInvalid

# Función que valida el request del servicio
    def validateRequest(self, request, headers):
        # Validacion del headers
        self.validateHeaders(headers)
        # Validacion del request
        validateSchema(request, sendMailSchema)

    # Función que reemplaza valores
    def replaceDataTemplate(self):
        for element in self.dictValues:
            self.template = self.template.replace(element, self.dictValues[element])
        return self.template

    # Función que construye el body del mensaje
    def constructMailBody(self):
        if self.headers["secret-x"] == SECRET_TOKEN_USER_NOT:
            with open('./templates/mail-users-not.html', 'r') as file:
                self.template = file.read()
            self.dictValues = {'{name}': self.data['name'], '{dni}': self.data['dni'],
                      '{ruv}': self.data['ruv'], '{estado}': self.data['estado'],
                      '{createAt}': self.data['createAt']}
        else:
            with open('./templates/mail-credit-card-not.html', 'r') as file:
                self.template = file.read()
            self.dictValues = {'{name}': self.data['name'], '{issuer}': self.data['issuer'],
                      '{lastfour}': self.data['lastFourDigits'], '{estado}': self.data['estado'],
                      '{createAt}': self.data['createAt']}
        return self.replaceDataTemplate()

    # Función que retorna el response por defecto
    def successResponse(self):
        return jsonify({'msg': 'Se envió email exitosamente'})

    # Función que realiza el envio del mail
    def send(self):
        msg = EmailMessage()
        message = self.constructMailBody()
        # Setup the parameters of the message
        password = MAIL_ACCOUNT_PASSWORD
        msg["From"] = MAIL_ACCOUNT_USER
        msg["To"] = self.data["emailTo"]
        msg["Subject"] = MAIL_SUBJECT
        # Add in the message body
        msg.add_header("Content-Type", "text/html")
        msg.set_payload(message)
        # Areate server
        server = smtplib.SMTP(MAIL_SMTP)
        server.starttls()
        # Login Credentials for sending the mail
        server.login(msg["From"], password)
        # send the message via the server.
        server.sendmail(msg["From"], msg["To"], msg.as_string())
        server.quit()

    # Función que realiza el envio
    def execute(self):
        try:
            self.send()
            logging.info(f"{LOG} Transaction response => ")
            logging.info(self.successResponse())
            return self.successResponse()
        except Exception as e:
            logging.error(e)
            raise ApiError(e)

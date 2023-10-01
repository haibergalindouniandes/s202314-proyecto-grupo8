# Importación de dependencias
from commands.base_command import BaseCommannd
from models.models import db, User
from errors.errors import ApiError, UserNameNotExists, PasswordNotExists, InvalidUserStatus
from validators.validators import validateSchema, generateTokenSchema
from datetime import datetime, timedelta
from sqlalchemy.exc import SQLAlchemyError
from utilities.utilities import formatDateTimeToUTC
from models.models import UserSchema
from flask.json import jsonify
import logging
import hashlib
import json
import uuid
import os

# Constantes
TOKEN_DURATION_MIN =  os.getenv("TOKEN_DURATION_MIN", default=360)
LOG = "[Authenticate]"

# Esquemas 
userSchema = UserSchema()

# Clase que contiene la logica de creción de usuarios
class Authenticate(BaseCommannd):
    def __init__(self, user):
        self.data = user
        self.validateRequest(user)

    # Función que valida si existe un usuario con el username
    def validateUserName(self, username):
        userToConsult = User.query.filter(User.username == username).first()
        if userToConsult == None:
            raise UserNameNotExists
        return userToConsult

    # Función que valida si existe un usuario con el password
    def validatePassword(self, username, password):
        userToConsult = User.query.filter(User.username == username, User.password == password).first()
        if userToConsult == None:
            raise PasswordNotExists

    # Función que permite generar el password
    def generatePassword(self, salt):
        return hashlib.sha512(self.password.encode('utf-8') + salt.encode('utf-8')).hexdigest()
    
    # Función que permite generar el token
    def generateToken(self):
        return uuid.uuid4()
    
    # Función que genera la fecha/hora actual + 15 minutos
    def generateExpirationDateTime(self):
        now = datetime.today()
        return now + timedelta(minutes=int(TOKEN_DURATION_MIN))
 
    # Función que valida el request del servicio
    def validateRequest(self, userJson):
        # Validacion del request
        validateSchema(userJson, generateTokenSchema)
        # Asignacion de variables
        self.username = userJson['username']
        self.password = userJson['password']

    # Función que valida el estado del usuario
    def validateUserStatus(self, userToUpdate):
        if userToUpdate.status != "VERIFICADO":
            userToUpdate.token = None
            userToUpdate.expireAt = None
            db.session.commit()
            logging.error(f"{LOG} User with status [{userToUpdate.status}]")
            logging.error(f"{LOG} User information [{userSchema.dump(userToUpdate)}]")
            raise InvalidUserStatus
    
    # Función que realiza la autenticación del usuario
    def execute(self):
        try:
            logging.info(f"{LOG} Variable [TOKEN_DURATION_MIN] => ")
            logging.info(TOKEN_DURATION_MIN)
            logging.info(f"{LOG} Transaction request => ")
            logging.info(self.data)
            userToUpdate = self.validateUserName(self.username)
            self.validateUserStatus(userToUpdate)
            password = self.generatePassword(userToUpdate.salt)
            self.validatePassword(self.username, password)
            userToUpdate.token = self.generateToken()
            userToUpdate.expireAt = self.generateExpirationDateTime()
            db.session.commit()
            userTokenResponse = {'id': str(userToUpdate.id), 'token': str(userToUpdate.token), 'expireAt': formatDateTimeToUTC(str(userToUpdate.createdAt))}
            logging.info(f"{LOG} Transaction response => ")
            logging.info(userTokenResponse)
            return jsonify(userTokenResponse)
        except SQLAlchemyError as e:# pragma: no cover
            logging.error(f"{LOG} Error => ")
            logging.error(e)
            raise ApiError(e)
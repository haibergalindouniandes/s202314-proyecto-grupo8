# Importación de dependencias
from commands.base_command import BaseCommannd
from models.models import db, User
from errors.errors import ApiError, UserNameNotExists, PasswordNotExists
from validators.validators import validateSchema, generateTokenSchema
from datetime import datetime, timedelta
from sqlalchemy.exc import SQLAlchemyError
import traceback
import hashlib
import uuid
import os

# Constantes
TOKEN_DURATION_MIN =  10
# Clase que contiene la logica de creción de usuarios
class Authenticate(BaseCommannd):
    def __init__(self, user):
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
    
    # Función que realiza la autenticación del usuario
    def execute(self):
        try:
            userToUpdate = self.validateUserName(self.username)
            password = self.generatePassword(userToUpdate.salt)
            self.validatePassword(self.username, password)
            userToUpdate.token = self.generateToken()
            userToUpdate.expireAt = self.generateExpirationDateTime()
            db.session.commit()
            return userToUpdate
        except SQLAlchemyError as e:# pragma: no cover
            traceback.print_exc()
            raise ApiError(e)
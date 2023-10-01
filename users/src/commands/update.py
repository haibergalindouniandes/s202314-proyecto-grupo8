# Importación de dependencias
import datetime
from commands.base_command import BaseCommannd
from errors.errors import ApiError, UserNameNotExists, BadRequest
from validators.validators import validateSchema, updateUserSchema
from models.models import UserSchema, db, User
from sqlalchemy.exc import SQLAlchemyError
import traceback
import logging

# Esquemas
userSchema = UserSchema()

# Constantes
LOG = "[Update User]"

# Clase que contiene la logica de creción de usuarios
class UpdateUser(BaseCommannd):
    def __init__(self, userId, data):
        self.data = data
        self.userId = userId
        self.dni = None
        self.fullName = None
        self.phoneNumber = None
        self.status = None
        self.validateRequest(data)

    # Función que valida si existe un usuario por el id
    def validateUser(self, userId):
        userToConsult = User.query.filter(User.id == userId).first()
        if userToConsult == None:
            raise UserNameNotExists
        return userToConsult

    # Función que valida el request del servicio
    def validateRequest(self, userJson):
        requestIsEmpty = True
        # Validacion del request
        validateSchema(userJson, updateUserSchema)
        # Asignacion de variables
        if "dni" in userJson:
            requestIsEmpty = False
            self.dni = userJson['dni'] 
        if "fullName" in userJson:
            requestIsEmpty = False
            self.fullName = userJson['fullName']
        if "phoneNumber" in userJson:
            requestIsEmpty = False
            self.phoneNumber = userJson['phoneNumber']
        if "status" in userJson:
            requestIsEmpty = False
            self.status = userJson['status'] 
        if requestIsEmpty:
            raise BadRequest

    # Función que realiza la actualización del usuario
    def execute(self):
        try:
            logging.info(f"{LOG} Transaction request => ")
            logging.info(self.data)
            userToUpdate = self.validateUser(self.userId)
            if self.dni != None:
                userToUpdate.dni = self.dni
            if self.fullName != None:
                userToUpdate.fullName = self.fullName
            if self.phoneNumber != None:
                userToUpdate.phoneNumber = self.phoneNumber
            if self.status != None:
                userToUpdate.status = self.status
            userToUpdate.updatedAt = datetime.datetime.now()
            db.session.commit()
            logging.info(f"{LOG} Transaction Response => ")
            logging.info(userSchema.dump(userToUpdate))
            return userToUpdate
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)
# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError, UserNameNotExists, BadRequest
from validators.validators import validateSchema, updateUserSchema
from models.models import db, User
from sqlalchemy.exc import SQLAlchemyError
import traceback

# Clase que contiene la logica de creción de usuarios
class UpdateUser(BaseCommannd):
    def __init__(self, userId, data):
        self.userId = userId
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
            userToUpdate = self.validateUser(self.userId)
            if self.dni:
                userToUpdate.dni = self.dni
            if self.fullName:
                userToUpdate.fullName = self.fullName
            if self.phoneNumber:
                userToUpdate.phoneNumber = self.phoneNumber
            if self.status:
                userToUpdate.status = self.status
            db.session.commit()
            return userToUpdate
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)
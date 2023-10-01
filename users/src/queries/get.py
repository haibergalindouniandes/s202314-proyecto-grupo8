# Importación de dependencias
from queries.base_query import BaseQuery
from errors.errors import ApiError, NotFound
from models.models import User, UserSchema
from sqlalchemy.exc import SQLAlchemyError
import logging

# Constantes
LOG = "[Get User By ID]"

# Esquemas
userSchema = UserSchema()

# Clase que contiene la logica de consulta de usuarios
class GetUserById(BaseQuery):
    def __init__(self, userId):
        self.userId = userId

    # Función que valida el token enviado
    def validateToken(self):
        userToConsult = User.query.filter(User.id == self.userId).first()
        if userToConsult == None:
            logging.error(f"{LOG} No se encontro un usuario con el ID [{self.userId}]")
            raise NotFound
        return userSchema.dump(userToConsult)

    # Función que realiza consulta de usuarios
    def query(self):
        try:
            return self.validateToken()
        except SQLAlchemyError as e:# pragma: no cover
            logging.error(e)
            raise ApiError(e)

# Importación de dependencias
import uuid
from queries.base_query import BaseQuery
from errors.errors import ApiError, InvalidToken, MissingToken, InvalidUserStatus, FormatTokenInvalid
from models.models import db, User, UserSchema
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import logging

# Constantes
LOG = "[User Detail]"

# Esquemas
userSchema = UserSchema()

# Clase que contiene la logica de creción de usuarios
class GetUserDetail(BaseQuery):
    def __init__(self, headers):
        logging.info(f"{LOG} Transaction request => ")
        logging.info(headers)
        self.validateHeaders(headers)
        self.validateIDsUUID(headers)

    # Función que valida el id en formato UUID
    def validateIDsUUID(self, value):
        try:
            uuid.UUID(str(value["Authorization"]).replace("Bearer ", ""))
        except Exception as e:
            logging.error(f"{LOG} Error [validateIDsUUID] => ")
            logging.error(FormatTokenInvalid.description)
            raise FormatTokenInvalid

    # Función que valida los headers
    def validateHeaders(self, headers):
        if not "Authorization" in headers:
            logging.error(f"{LOG} Error [validateHeaders] => ")
            logging.error(MissingToken.description)
            raise MissingToken
        self.token = headers["Authorization"]

    # Función que valida el token enviado
    def validateToken(self):
        userToConsult = User.query.filter(User.token == self.token.replace("Bearer ", "")).first()
        if userToConsult == None:
            logging.error(f"{LOG} Token [{userToConsult.status}] invalid")
            raise InvalidToken
        if userToConsult.status != "VERIFICADO":
            userToConsult.token = None
            userToConsult.expireAt = None
            db.session.commit()
            logging.error(f"{LOG} User with status [{userToConsult.status}]")
            logging.error(f"{LOG} User information [{userSchema.dump(userToConsult)}]")
            raise InvalidUserStatus
        
        expireAt = userToConsult.expireAt
        currentDateTime = datetime.today()
        if expireAt < currentDateTime:
            raise InvalidToken# pragma: no cover
        logging.info(f"{LOG} Transaction response => ")
        logging.info(userSchema.dump(userToConsult))
        return userSchema.dump(userToConsult)

    # Función que realiza consulta de usuarios
    def query(self):
        try:
            return self.validateToken()
        except SQLAlchemyError as e:# pragma: no cover
            logging.error(f"{LOG} Error [SQLAlchemyError] => ")
            logging.error(e)
            raise ApiError(e)

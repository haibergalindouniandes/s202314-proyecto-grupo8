# Importación de dependencias
from queries.base_query import BaseQuery
from errors.errors import ApiError, InvalidToken, MissingToken
from models.models import Route
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import traceback

# Clase que contiene la logica de creción de usuarios
class GetRouteDetail(BaseQuery):
    def __init__(self, headers):
        self.validateHeaders(headers)

    # Función que valida los headers
    def validateHeaders(self, headers):
        if not "Authorization" in headers:
            raise MissingToken
        self.token = headers["Authorization"]


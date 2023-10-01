# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError,  BadRequest
from validators.validators import validateSchema
from models.models import db, Route
from sqlalchemy.exc import SQLAlchemyError
import traceback

# Clase que contiene la logica de creción de usuarios
class UpdateRoute(BaseCommannd):
    def __init__(self, flightId, data):
        self.flightId = flightId
        self.validateRequest(data)

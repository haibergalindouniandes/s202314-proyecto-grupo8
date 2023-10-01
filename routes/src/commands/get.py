# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError,  NotFound, IdNotUUID, NotFound
from validators.validators import validateSchema, createRouteSchema,validateIDsUUID
from models.models import db, Route
from sqlalchemy.exc import SQLAlchemyError
import traceback


# Clase que contiene la logica de consulta de Rutas
class GetRoute(BaseCommannd):
    def __init__(self, id):
        self.id = id

    # Función que realiza consulta
    def execute(self):
        try:
            validateIDsUUID(self.id)
            routeToConsult = Route.query.filter(Route.id == self.id).first()
            if routeToConsult is None:
                raise NotFound
            return  routeToConsult
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)
        except IdNotUUID as e:
            traceback.print_exc()
            raise IdNotUUID(e)
        except NotFound as e:
            traceback.print_exc()
            raise NotFound(e)
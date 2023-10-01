# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError, NotFound,IdNotUUID
from models.models import db, Route
from sqlalchemy.exc import SQLAlchemyError
from validators.validators import validateIDsUUID, validateSchema, createRouteSchema
import traceback


# Clase que contiene la logica de eliminacion de trayectos
class DeleteRoute(BaseCommannd):
    def __init__(self, id):
        self.id = id


    # Función que realiza eliminacion de un trayecto
    def execute(self):
        try:
            validateIDsUUID(self.id)
            idToConsult = Route.query.filter(Route.id == self.id).first()
            if idToConsult == None:
                raise NotFound
            Route.query.filter(Route.id == self.id).delete()
            db.session.commit()
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)
        except IdNotUUID as e:
            traceback.print_exc()
            raise IdNotUUID(e)
        except NotFound as e:
            traceback.print_exc()
            raise NotFound(e)
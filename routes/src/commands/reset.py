# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError
from models.models import db, Route
import traceback

# Clase que contiene la logica de creción de trayectos
class ResetRoutes(BaseCommannd):
    # Función que realiza creación del trayecto
    def execute(self):
        try:
            db.session.query(Route).delete()
            db.session.commit()
        except Exception as e:
            traceback.print_exc()
            raise ApiError(e)
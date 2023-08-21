# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError
from models.models import db, User
import traceback

# Clase que contiene la logica de creción de usuarios
class ResetUsers(BaseCommannd):
    # Función que realiza creación del usuario
    def execute(self):
        try:
            db.session.query(User).delete()
            db.session.commit()
        except Exception as e:# pragma: no cover
            traceback.print_exc()
            raise ApiError(e)
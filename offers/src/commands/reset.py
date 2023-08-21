# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError
from models.models import db, Offer
import traceback

# Clase que contiene la logica de creción de usuarios
class ResetOffers(BaseCommannd):
    # Función que realiza creación del usuario
    def execute(self):
        try:
            db.session.query(Offer).delete()
            db.session.commit()
        except Exception as e:
            traceback.print_exc()
            raise ApiError(e)
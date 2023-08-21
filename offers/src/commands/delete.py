# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError, NotFound
from models.models import db, Offer
from sqlalchemy.exc import SQLAlchemyError
from validators.validators import validateIDsUUID
import traceback


# Clase que contiene la logica de creción de usuarios
class DeleteOffer(BaseCommannd):
    def __init__(self, offerId):
        self.offerId = offerId


    # Función que realiza creación del usuario
    def execute(self):
        try:
            validateIDsUUID(self.offerId)
            idToConsult = Offer.query.filter(Offer.id == self.offerId).first()
            if idToConsult == None:
                raise NotFound
            Offer.query.filter(Offer.id == self.offerId).delete()
            db.session.commit()
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)
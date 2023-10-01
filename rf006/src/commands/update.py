from commands.base_command import BaseCommannd
from errors.errors import ApiError
from models.models import db, TarjetaCredito
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import traceback


class TarjetaCreditoUpdate(BaseCommannd):
    def __init__(self, id, status):
        self.id = id
        self.status = status
                    
    def execute(self):
        try:
            card_to_update = TarjetaCredito.query.filter(TarjetaCredito.id == self.id).first()
            card_to_update.status = self.status
            card_to_update.updatedAt = datetime.now()
            db.session.commit()
            return card_to_update
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)
        
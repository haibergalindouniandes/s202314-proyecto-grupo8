from commands.base_command import BaseCommannd
from errors.errors import ApiError
from models.models import db, TarjetaCredito
from sqlalchemy.exc import SQLAlchemyError
import traceback


class TarjetaCreditoOnProcess(BaseCommannd):
    def __init__(self, status):
        self.status = status
                    
    def execute(self):
        try:
            cards_on_process = TarjetaCredito.query.filter(TarjetaCredito.status == self.status)
            return cards_on_process
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)
        

class TarjetaCreditoUsuario(BaseCommannd):
    def __init__(self, userId):
        self.userId = userId
                    
    def execute(self):
        try:
            cards_on_process = TarjetaCredito.query.filter(TarjetaCredito.userId == self.userId)
            result_dict = [u.__dict__ for u in cards_on_process]
            for tarjeta in result_dict:
                del tarjeta['ruv']
            return result_dict
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)
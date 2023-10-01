from commands.base_command import BaseCommannd
from commands.registration import RegistrarTarjetaCredito
from errors.errors import ApiError
from validators.validators import CrearTarjetaSchema, validateSchema, validateCreditCard, validateExpirationDate, validateTrueNativeToken
from models.models import db, TarjetaCredito
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
import traceback
import uuid


class CrearTarjetaCredito(BaseCommannd):
    def __init__(self, userId, post_request_json):
        self.validateRequest(userId, post_request_json)
        
   
    def validateRequest(self, userId, post_request_json):
        validateSchema(post_request_json, CrearTarjetaSchema)        
        validateExpirationDate(post_request_json['expirationDate'])
        self.id = str(uuid.uuid1())
        self.userId = userId
        self.cardNumber = post_request_json['cardNumber']
        self.cvv = post_request_json['cvv']
        self.expirationDate = post_request_json['expirationDate']
        self.cardHolderName = post_request_json['cardHolderName']
        self.createdAt = datetime.now()
        self.resp_trueNative = self.registrarTarjeta()
        validateTrueNativeToken(self.resp_trueNative)
        validateCreditCard(self.resp_trueNative)


    def registrarTarjeta(self):
        registrarTarjetaObj = RegistrarTarjetaCredito(cardNumber=self.cardNumber, cvv=self.cvv, expirationDate=self.expirationDate, cardHolderName=self.cardHolderName)
        respuesta = registrarTarjetaObj.execute()
        return respuesta
        
            
    def execute(self):
        try:
            new_creditCard = TarjetaCredito(id=self.id,
                                            token=self.resp_trueNative.json()['token'],
                                            userId=self.userId,
                                            lastFourDigits=self.cardNumber[-4:],
                                            ruv=self.resp_trueNative.json()['RUV'],
                                            issuer=self.resp_trueNative.json()['issuer'],
                                            status='POR_VERIFICAR',
                                            createdAt=self.createdAt
                                           )
            db.session.add(new_creditCard)
            db.session.commit()            
            return {'id':self.id, 'userId':self.userId, 'createdAt':self.createdAt.replace(microsecond=0).isoformat()}
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)
        
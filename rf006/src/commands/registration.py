# Importación de dependencias
from commands.base_command import BaseCommannd
from os import environ as env
import requests
import json
import uuid


class RegistrarTarjetaCredito(BaseCommannd):
    def __init__(self, cardNumber, cvv, expirationDate, cardHolderName):
        self.cardNumber = cardNumber
        self.cvv = cvv
        self.expirationDate = expirationDate
        self.cardHolderName = cardHolderName

    
    def execute(self):
        TRUENATIVE_PATH = env["TRUENATIVE_PATH"]
        TRUENATIVE_TOKEN = env["TRUENATIVE_TOKEN"]
        card = {"cardNumber":self.cardNumber,
                "cvv":self.cvv,
                "expirationDate":self.expirationDate,
                "cardHolderName":self.cardHolderName
               }
        data = {"card":card, "transactionIdentifier":str(uuid.uuid1())}
        try:
            respuesta = requests.post(f'{TRUENATIVE_PATH}/native/cards', json=data, headers={"Authorization":f"Bearer {TRUENATIVE_TOKEN}"})            
            return respuesta
        except Exception as e:
            print(e)
        
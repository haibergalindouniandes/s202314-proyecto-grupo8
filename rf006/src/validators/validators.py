from errors.errors import BadRequest, InvalidToken, MissingToken, CreditCardExpired, CreditCardRepeated, MissingTrueNativeToken, ApiError
from models.models import db, TarjetaCredito
from sqlalchemy.exc import SQLAlchemyError
from jsonschema import validate
from datetime import datetime
from dateutil.parser import parse, ParserError
from dateutil.relativedelta import relativedelta
import traceback
import jsonschema
import requests
import os


CrearTarjetaSchema = {
    "type": "object",
    "properties": {
        "cardNumber": {"type": "string", "minimum": 15, "maximum": 16, "pattern": "^\d{15,16}$"},
        "cvv": {"type": "string", "minimum": 3, "maximum": 4, "pattern": "^\d{3,4}$"},
        "expirationDate":  {"type": "string", "minimum": 5, "maximum": 5, "pattern": "^\d{2}/\d{2}$"},
        "cardHolderName": {"type": "string", "minimum": 4, "maximum": 20}
    },
    "required": ["cardNumber","cvv","expirationDate","cardHolderName"]
}


def validateSchema(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        traceback.print_exc()
        raise BadRequest
    

def validateToken(headers):
    USERS_PATH = os.environ["USERS_PATH"]
    # call user/me
    result =  requests.get(USERS_PATH+'/users/me', headers=headers)
    if result.status_code == 401:
        traceback.print_exc()
        raise InvalidToken
    if result.status_code == 403:
        traceback.print_exc()
        raise MissingToken
    return result.json()["id"]


def validateExpirationDate(strDate):
    try:
        strDate = f'{strDate}/01'
        date = parse(strDate, yearfirst=True)
        expDate = date + relativedelta(months=1)
        if expDate <= datetime.now():
            raise CreditCardExpired
    except ParserError:
        traceback.print_exc()
        raise BadRequest


def validateTrueNativeToken(resp_trueNative):
    if resp_trueNative.json()['token'] is None:
        raise MissingTrueNativeToken


def validateCreditCard(resp_trueNative):
    try:
        token = resp_trueNative.json()['token']        
        credit_card = TarjetaCredito.query.filter(TarjetaCredito.token == token).first()
        if credit_card is not None:
           raise CreditCardRepeated
    except SQLAlchemyError as e:
        traceback.print_exc()
        raise ApiError(e)



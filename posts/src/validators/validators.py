# Importación de dependencias
import traceback
import jsonschema
import requests
from jsonschema import validate
from errors.errors import BadRequest, MissingToken, InvalidToken, InvalidUUID, InvalidExpirationDate
from dateutil.parser import parse, ParserError
from datetime import datetime
import uuid
import os


# Esquema para la creación de publicaciones
createPostSchema = {
    "type": "object",
    "properties": {
        "routeId": {"type": "string", "minimum": 36, "maximum": 36},
        "expireAt":  {"type": "string", "minimum": 19, "maximum": 26}
    },
    "required": ["routeId", "expireAt"]
}

# Función que valida el request para la creación de publicacion
def validateSchema(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        traceback.print_exc()
        raise BadRequest

# Función que valida string con formato uuid
def validateUUID(value):
    try:
        uuid.UUID(str(value))
    except ValueError:
        traceback.print_exc()
        raise InvalidUUID
    
# Funcion que valida si un string es un tipo de dato fecha y es una fecha de expiracion valida
def validateDateString(value):
    try:        
        value = value.replace("Z", "")
        fecha = parse(value)
        if fecha <= datetime.now():
            raise InvalidExpirationDate
    except ParserError:
        traceback.print_exc()
        raise InvalidExpirationDate

# Función que valida los headers
def validateToken(headers):
    USERS_PATH = os.environ["USERS_PATH"]    
    result =  requests.get(f"{USERS_PATH}/users/me", headers=headers)
    if result.status_code == 401:
        traceback.print_exc()
        raise InvalidToken
    if result.status_code == 403:
        traceback.print_exc()
        raise MissingToken
    return result.json()["id"]
        
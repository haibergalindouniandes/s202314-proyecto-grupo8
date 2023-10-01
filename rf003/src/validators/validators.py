import traceback
from errors.errors import BadRequest, InvalidToken, MissingToken
import os
import requests
from datetime import datetime
import jsonschema
from jsonschema import validate


rf003Schema = {
    "type": "object",
    "properties": {
        "flightId": {"type": "string", "minimum": 1, "maximum": 5},
        "expireAt": {"type": "string", "minimum": 19, "maximum": 26},
        "plannedStartDate": {"type": "string", "minimum": 1, "maximum": 100},
        "plannedEndDate": {"type": "string", "minimum": 1, "maximum": 100},
        "origin": {
            "airportCode": {"type": "string", "minimum": 3, "maximum": 3},
            "country": {"type": "string", "minimum": 1, "maximum": 100},
        },
        "destiny": {
            "airportCode": {"type": "string", "minimum": 3, "maximum": 3},
            "country": {"type": "string", "minimum": 1, "maximum": 100},
        },
        "bagCost": {"type": "integer"},
    },
    "required": [
        "flightId",
        "expireAt",
        "plannedStartDate",
        "plannedEndDate",
        "bagCost",
        "origin",
        "destiny",
    ],
}

# Función que valida el request para rf003
def validateSchema(jsonData):
    try:
        validate(instance=jsonData, schema=rf003Schema)
    except jsonschema.exceptions.ValidationError as err:
        traceback.print_exc()
        raise BadRequest


# Función que valida los headers
def validateToken(headers):
    USERS_PATH = os.environ["USERS_PATH"]
    # call user/me
    result = requests.get(USERS_PATH + "/users/me", headers=headers)
    if result.status_code == 401:
        traceback.print_exc()
        raise InvalidToken
    if result.status_code == 403:
        traceback.print_exc()
        raise MissingToken
    return result.json()["id"]


# Funcion que valida las fechas
def validateDates(dateFlight, dateExpirePost):
    formatting = "%Y-%m-%dT%H:%M:%S.%fZ"
    dateF = datetime.strptime(dateFlight, formatting)
    dateP = datetime.strptime(dateExpirePost, formatting)
    actualDate = datetime.now()
    if (dateF > actualDate) and (dateP <= dateF):
        return True
    else:
        return False


# Funcion que valida la fecha de expiracion
def validate_expiration_date(dateExpirePost):
    formatting = "%Y-%m-%dT%H:%M:%S.%fZ"
    dateP = datetime.strptime(dateExpirePost, formatting)
    actualDate = datetime.now()
    if dateP > actualDate:
        return True
    else:
        return False

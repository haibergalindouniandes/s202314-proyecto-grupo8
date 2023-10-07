# Importación de dependencias
from errors.errors import BadRequest
from jsonschema import validate
import jsonschema
import logging

# Esquemas
# Esquema para el envio del email
sendMailSchema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minimum": 4, "maximum": 64},
        "dni": {"type": "string", "minimum": 4, "maximum": 64},
        "ruv": {"type": "string", "minimum": 4, "maximum": 64},
        "estado": {"type": "string", "minimum": 4, "maximum": 64},
        "createAt": {"type": "string", "minimum": 4, "maximum": 64},
        "emailTo": {"type": "string", "minimum": 4, "maximum": 64},
        "issuer": {"type": "string", "minimum": 4, "maximum": 64},
        "lastFourDigits": {"type": "string", "minimum": 4, "maximum": 4},
    },
    "required": ["name", "estado", "createAt", "emailTo"]
}

# Función que valida el request para la creación de usuarios
def validateSchema(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        logging.error(err)
        raise BadRequest
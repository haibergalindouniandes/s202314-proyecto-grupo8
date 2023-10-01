# Importación de dependencias
from errors.errors import BadRequest, BadUuid
from jsonschema import validate
from uuid import UUID
import traceback
import jsonschema

# Esquema para la creación de scores
createScoreSchema = {
    "type": "object",
    "properties": {
        "packageDescription": {"type": "string", "minimum": 4, "maximum": 200},
        "packageSize": {"type": "string", "enum": ["LARGE", "MEDIUM", "SMALL"]},
        "packageAmount":  {"type": "string", "pattern": "-?^\\d*(.\\d{0,2})?$"},
        "isPackageFragile": {"type": "boolean"},
        "offerAmount":  {"type": "string", "pattern": "-?^\\d*(.\\d{0,2})?$"},
        "offerId": {"type": "string", "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"},
        "postId": {"type": "string", "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"},
        "userId": {"type": "string", "pattern": "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"},
    },
    "required": ["packageDescription", "packageSize", "packageAmount", "isPackageFragile", "offerAmount", "offerId", "postId", "userId"]
}

# Función que valida la estructura de un esquema
def validateSchema(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        traceback.print_exc()
        raise BadRequest

# Función que valida la estructura de un uuid
def validateUuid(uuid):
    try:
        UUID(uuid)
    except:
        raise BadUuid

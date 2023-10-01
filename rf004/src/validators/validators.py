# Importación de dependencias
import traceback
import jsonschema
import requests
from jsonschema import validate
from errors.errors import BadRequest, InvalidToken, MissingToken, PostDoNotExist, PostExpired, PostInvalidOwner
import os

# Esquema para la creación de ofertas
createOfferSchema = {
    "type": "object",
    "properties": {        
        "description": {"type": "string", "minimum": 4, "maximum": 140},
        "size":  {"type": "string", "enum": ["LARGE", "MEDIUM", "SMALL"]},
        "fragile": {"type": "boolean"},
        "offer": {"type": "number", "minimum": 0},
    },
    "required": ["description","size","fragile","offer"]
}
# Función que valida el request para la creación de oferta
def validateSchema(jsonData, schema):
    try:
        validate(instance=jsonData, schema=schema)
    except jsonschema.exceptions.ValidationError as err:
        traceback.print_exc()        
        raise BadRequest

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

# Función que valida que una Publicacion existe
def validatePostId(id, headers):
    POSTS_PATH = os.environ["POSTS_PATH"]
    result =  requests.get(f"{POSTS_PATH}/posts/{id}", headers=headers)
    if result.status_code == 400 or result.status_code == 404:
        traceback.print_exc()
        raise PostDoNotExist
    return result

# Función que valida que una Publicacion no ha expirado
def validatePostExpired(id, headers):
    POSTS_PATH = os.environ["POSTS_PATH"]
    result =  requests.get(f"{POSTS_PATH}/posts?expire=true", headers=headers)
    posts = result.json()
    id_posts = [post['id'] for post in posts]
    if id in id_posts:
        traceback.print_exc()
        raise PostExpired

# Función que valida que una Publicacion no pertenece al mismo usuario
def validatePostOwner(id, headers):
    POSTS_PATH = os.environ["POSTS_PATH"]
    result =  requests.get(f"{POSTS_PATH}/posts?owner=me", headers=headers)
    posts = result.json()
    id_posts = [post['id'] for post in posts]
    if id in id_posts:
        traceback.print_exc()
        raise PostInvalidOwner
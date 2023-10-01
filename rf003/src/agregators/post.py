# Importación de dependencias
from flask.json import jsonify
import os
import requests
from errors.errors import ApiError
import traceback
from rollbacks.routes import RF003CreateRouteRollback


# Funcion que verifica que el usuario no haya creado otra publicacion para la misma ruta
def post_user_route_check(routeId, userId, headers):
    POSTS_PATH = os.environ["POSTS_PATH"]
    result = requests.get(
        POSTS_PATH + "/posts?route=" + routeId + "&owner=" + userId, headers=headers
    )
    respuesta = result.json()
    if len(respuesta) == 0:
        return True
    return False


# Funcion para creacion de Post con los valores dados
def rf003_post_create(routeid, expireDate, headers):
    try:
        POSTS_PATH = os.environ["POSTS_PATH"]
        info = {"routeId": routeid, "expireAt": expireDate}
        result = requests.post(POSTS_PATH + "/posts", json=info, headers=headers)
        if result.status_code != 201:
            RF003CreateRouteRollback().execute(headers, routeid)
            raise ApiError
        return result.json() 
    except ApiError as e:
            traceback.print_exc()
            raise ApiError(e)
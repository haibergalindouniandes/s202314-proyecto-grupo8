# Importación de dependencias
import os
import traceback
import requests
from errors.errors import ApiError, RouteDateError
from rollbacks.routes import RF003CreateRouteRollback

# funcion que valida si el route existe
def route_check(data, headers):
    try:
        ROUTES_PATH = os.environ["ROUTES_PATH"]
        result = requests.get(
            ROUTES_PATH + "/routes?flight=" + data["flightId"], headers=headers
        )
        respuesta = result.json()
        if len(respuesta) == 0:
            body = {
                "flightId": data["flightId"],
                "sourceAirportCode": data["origin"]["airportCode"],
                "sourceCountry": data["origin"]["country"],
                "destinyAirportCode": data["destiny"]["airportCode"],
                "destinyCountry": data["destiny"]["country"],
                "bagCost": data["bagCost"],
                "plannedStartDate": data["plannedStartDate"],
                "plannedEndDate": data["plannedEndDate"],
            }
            creation = requests.post(
                ROUTES_PATH + "/routes", json=body, headers=headers
            )
            if 412 == creation.status_code:
                raise RouteDateError
            RF003CreateRouteRollback().set_flag()
            return creation.json()
        elif 200 == result.status_code:
            RF003CreateRouteRollback().clear_flag()
            return respuesta[0]
        else:
            raise ApiError
    except RouteDateError as e:
        traceback.print_exc()
        raise RouteDateError(e)
    except ApiError as e:
        traceback.print_exc()
        raise ApiError(e)
    

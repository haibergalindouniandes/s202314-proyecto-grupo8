import requests
import os


flag = None


class RF003CreateRouteRollback:
    def clear_flag(self):
        print("Flag en Falso por funcion")
        global flag
        flag = False

    def set_flag(self):
        global flag
        flag = True
        print("Flag Lista para el rollback flag = " + str(flag))

    def execute(self, header, routeId):
        print("Dentro del rollback - flag =  " + str(flag))
        if flag:
            ROUTES_PATH = os.environ["ROUTES_PATH"]
            result = requests.delete(ROUTES_PATH + "/routes/" + routeId, headers=header)
            print("Rollback de route: " + routeId)
            print("Resultado de Rollback: " + str(result.status_code))

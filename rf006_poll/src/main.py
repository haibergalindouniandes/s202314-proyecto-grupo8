from flask import Flask
import requests
import time
import threading
from os import environ as env
import os
from requests.structures import CaseInsensitiveDict

app = Flask(__name__)

EMAIL_TOKEN = os.getenv("EMAIL_TOKEN", default="d5f14860-f674-4248-be61-18bed307a4a0")
APP_PORT =  int(os.getenv("APP_PORT", default=3000))

@app.route("/poll/ping", methods=["GET"])
def health():
    return "pong"

# Función que construye el request de SendEmail
def constructRequest(user, truenative, tarjeta):
    return {
        "name": f"{user['username']}",
        "lastFourDigits": f"{tarjeta['lastFourDigits']}",
        "issuer": f"{tarjeta['issuer']}",
        "estado": f"{truenative['status']}",
        "createAt": f"{truenative['createdAt']}",
        "emailTo": f"{user['email']}",
    }


def estado_solicitud():
    RF006_PATH = env["RF006_PATH"]
    USERS_PATH = env["USERS_PATH"]
    TRUENATIVE_PATH = env["TRUENATIVE_PATH"]
    TRUENATIVE_TOKEN = env["TRUENATIVE_TOKEN"]
    SEND_EMAIL_PATH = env["SEND_EMAIL_PATH"]
    resp_tarjetas_por_verificar = requests.get(f"{RF006_PATH}/credit-cards/on-process")

    for tarjeta in resp_tarjetas_por_verificar.json():
        ruv = tarjeta["ruv"]
        resp_trueNative = requests.get(
            f"{TRUENATIVE_PATH}/native/cards/{ruv}",
            headers={"Authorization": f"Bearer {TRUENATIVE_TOKEN}"},
        )
        print(resp_trueNative.status_code)
        if resp_trueNative.status_code == 200:
            tarjeta_id = tarjeta["id"]
            new_status = resp_trueNative.json()["status"]
            data = {"id": tarjeta_id, "status": new_status}
            # Se actualiza base de datos
            resp_actualizar_tarjeta = requests.post(
                f"{RF006_PATH}/credit-cards/update", json=data
            )
            # Se envia correo
            infousers = requests.get(f"{USERS_PATH}/users/{tarjeta['userId']}")
            headers = CaseInsensitiveDict()
            headers["secret-x"] = EMAIL_TOKEN
            requestSendEmail = constructRequest(
                infousers.json(), resp_trueNative.json(), tarjeta
            )
            responseSendEmail = requests.post(
                SEND_EMAIL_PATH, json=requestSendEmail, headers=headers
            )
            if responseSendEmail.status_code != 200:
                resp_actualizar_tarjeta = "Error al enviar el correo"
        elif resp_trueNative.status_code == 202:
            resp_actualizar_tarjeta = "Solicitud en proceso"
        elif resp_trueNative.status_code == 404:
            resp_actualizar_tarjeta = (
                "No existe una verificación en proceso con ese RUV"
            )
        return resp_actualizar_tarjeta


def timer():
    while True:
        try:
            print("<=================================>")
            respuesta = estado_solicitud()
            if respuesta is None:
                print(
                    f"Connection established --> No hay solicitudes en proceso",
                    flush=True,
                )
            elif isinstance(respuesta, requests.Response):
                print(
                    f'Connection established --> card id: {respuesta.json()["id"]}, new status: {respuesta.json()["status"]}',
                    flush=True,
                )
            else:
                print(f"Connection established --> {respuesta}", flush=True)
        except:
            print("Connection NOT established", flush=True)
        time.sleep(1)


t = threading.Thread(target=timer)
t.start()
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=APP_PORT)

from flask import request, Blueprint
from commands.sendmail import SendMail

users_blueprint = Blueprint('send', __name__)

# Recurso que expone la funcionalidad healthcheck
@users_blueprint.route('/send/ping', methods=['GET'])
def health():
    return "pong"

# Recurso que expone la funcionalidad authenticate
@users_blueprint.route('/send/mail', methods=['POST'])
def sendMail():
    data = request.get_json()
    headers = request.headers
    return SendMail(data, headers).execute()


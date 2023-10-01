from flask import request, Blueprint
from flask.json import jsonify
from commands.create import CrearTarjetaCredito
from commands.query import TarjetaCreditoOnProcess, TarjetaCreditoUsuario
from commands.update import TarjetaCreditoUpdate
from commands.reset import ResetCards
from models.models import TarjetaCreditoSchema
from validators.validators import validateToken


tarjetaCredito_blueprint = Blueprint('tarjetaCredito', __name__)
tarjeta_schema = TarjetaCreditoSchema()

@tarjetaCredito_blueprint.route('/credit-cards', methods=['POST'])
def create():
    userId = validateToken(request.headers)
    creditCardObj = CrearTarjetaCredito(userId=userId, post_request_json=request.get_json())
    creditCard_resp = creditCardObj.execute()
    return jsonify(creditCard_resp), 201


@tarjetaCredito_blueprint.route('/credit-cards', methods=['GET'])
def get():
    userId = validateToken(request.headers)
    cardUserObj = TarjetaCreditoUsuario(userId=userId)
    tarjetas_user = cardUserObj.execute()
    return [tarjeta_schema.dump(tarjeta) for tarjeta in tarjetas_user], 200

@tarjetaCredito_blueprint.route('/credit-cards/ping', methods=['GET'])
def health():
    return "pong"

@tarjetaCredito_blueprint.route('/credit-cards/reset', methods=['POST'])
def reset():
    ResetCards().execute()
    return jsonify({'msg': 'Todos los datos fueron eliminados'}), 200

@tarjetaCredito_blueprint.route('/credit-cards/on-process', methods=['GET'])
def query():
    cardOnProcessObj = TarjetaCreditoOnProcess(status='POR_VERIFICAR')
    tarjetas_resp = cardOnProcessObj.execute()
    return [tarjeta_schema.dump(tarjeta) for tarjeta in tarjetas_resp], 200

@tarjetaCredito_blueprint.route('/credit-cards/update', methods=['POST'])
def update():
    id = request.get_json()['id']
    status = request.get_json()['status']
    cardUpdateObj = TarjetaCreditoUpdate(id=id, status=status)
    cardUpdate_resp = cardUpdateObj.execute()
    return tarjeta_schema.dump(cardUpdate_resp), 200

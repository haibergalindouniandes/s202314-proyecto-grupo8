from flask import request, Blueprint
from flask.json import jsonify
from commands.create import CreateOffer
from commands.reset import ResetOffers
from commands.delete import DeleteOffer
from commands.get import GetOffer
from commands.list import ListOffer
from utilities.utilities import formatDateTimeToUTC
from validators.validators import validateToken

offers_blueprint = Blueprint('offers', __name__)

@offers_blueprint.route('/offers/ping', methods=['GET'])
def health():
    return "pong"

@offers_blueprint.route('/offers/reset', methods=['POST'])
def reset():
    ResetOffers().execute()
    return jsonify({'msg': 'Todos los datos fueron eliminados'})

@offers_blueprint.route('/offers', methods=['POST'])
def create():
    data = request.headers
    user = validateToken(data)
    data = request.get_json()
    result = CreateOffer(data, user).execute()
    return jsonify({'id': result.id,'userId': result.userId, 'createdAt': formatDateTimeToUTC(str(result.createdAt))}), 201

@offers_blueprint.route('/offers/<string:id>', methods=['DELETE'])
def delete(id):
    data = request.headers
    validateToken(data)
    DeleteOffer(id).execute()
    return jsonify({'msg': 'la oferta fue eliminada'}), 200

@offers_blueprint.route('/offers/<string:id>', methods=['GET'])
def get(id):
    data = request.headers
    validateToken(data)
    result = GetOffer(id).execute()
    return jsonify({'id': result.id, 'postId': result.postId, 'description': result.description, 'size': result.size, 'fragile': result.fragile, 'offer': result.offer, 'createdAt': result.createdAt, 'userId': result.userId}), 200

@offers_blueprint.route('/offers', methods=['GET'])
def listOffer():
    post = request.args.get('post', None)
    owner = request.args.get('owner', None)
    data = request.headers
    if owner == 'me':
        owner = validateToken(data)
    else:
        validateToken(data)
    result = ListOffer(post, owner).execute()
    return jsonify(result)
from flask import request, Blueprint
from flask.json import jsonify
from commands.create import CreateUser
from commands.reset import ResetUsers
from commands.authenticate import Authenticate
from queries.detail import GetUserDetail
from commands.update import UpdateUser
from utilities.utilities import formatDateTimeToUTC

users_blueprint = Blueprint('posts', __name__)

@users_blueprint.route('/posts/ping', methods=['GET'])
def health():
    return "pong"

@users_blueprint.route('/posts/reset', methods=['POST'])
def reset():
    ResetUsers().execute()
    return jsonify({'msg': 'Todos los datos fueron eliminados'})

@users_blueprint.route('/posts/auth', methods=['POST'])
def authenticate():
    data = request.get_json()
    result = Authenticate(data).execute()
    return jsonify({'id': result.id, 'token': result.token, 'expireAt': formatDateTimeToUTC(str(result.createdAt))})

@users_blueprint.route('/posts/me', methods=['GET'])
def detail():
    data = request.headers
    result = GetUserDetail(data).query()
    return jsonify({'id': result.id, 'username': result.username, 'email': result.email, 'fullName': result.fullName, 'dni': result.dni, 'phoneNumber': result.phoneNumber, 'status': result.status})

@users_blueprint.route('/posts/<string:userId>', methods=['PATCH'])
def update(userId):
    data = request.get_json()
    UpdateUser(userId, data).execute()
    return jsonify({'msg': 'el usuario ha sido actualizado'})

@users_blueprint.route('/posts', methods=['POST'])
def create():
    data = request.get_json()
    result = CreateUser(data).execute()
    return jsonify({'id': result.id, 'createdAt': formatDateTimeToUTC(str(result.createdAt))}), 201
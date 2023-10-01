from flask import request, Blueprint
from flask.json import jsonify
from commands.create import CreateUser
from commands.reset import ResetUsers
from commands.authenticate import Authenticate
from queries.detail import GetUserDetail
from commands.update import UpdateUser
from utilities.utilities import formatDateTimeToUTC

users_blueprint = Blueprint('users', __name__)

# Recurso que expone la funcionalidad healthcheck
@users_blueprint.route('/users/ping', methods=['GET'])
def health():
    return "pong"

# Recurso que expone la funcionalidad reset users
@users_blueprint.route('/users/reset', methods=['POST'])
def reset():
    ResetUsers().execute()
    return jsonify({'msg': 'Todos los datos fueron eliminados'})

# Recurso que expone la funcionalidad authenticate
@users_blueprint.route('/users/auth', methods=['POST'])
def authenticate():
    data = request.get_json()
    result = Authenticate(data).execute()
    return jsonify({'id': result.id, 'token': result.token, 'expireAt': formatDateTimeToUTC(str(result.createdAt))})

# Recurso que expone la funcionalidad detail user
@users_blueprint.route('/users/me', methods=['GET'])
def detail():
    data = request.headers
    result = GetUserDetail(data).query()
    return jsonify({'id': result.id, 'username': result.username, 'email': result.email, 'fullName': result.fullName, 'dni': result.dni, 'phoneNumber': result.phoneNumber, 'status': result.status})

# Recurso que expone la funcionalidad update user
@users_blueprint.route('/users/<string:userId>', methods=['PATCH'])
def update(userId):
    data = request.get_json()
    UpdateUser(userId, data).execute()
    return jsonify({'msg': 'el usuario ha sido actualizado'})

# Recurso que expone la funcionalidad create user
@users_blueprint.route('/users', methods=['POST'])
def create():
    data = request.get_json()
    result = CreateUser(data).execute()
    return jsonify({'id': result.id, 'createdAt': formatDateTimeToUTC(str(result.createdAt))}), 201
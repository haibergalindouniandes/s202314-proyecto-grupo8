from flask import request, Blueprint
from flask.json import jsonify
from commands.create import CreateUser
from commands.reset import ResetUsers
from commands.authenticate import Authenticate
from queries.detail import GetUserDetail
from commands.update import UpdateUser
from commands.verify import VerifyUser
from queries.get import GetUserById
from utilities.utilities import formatDateTimeToUTC
from externals.truenative import verifyUserExternal

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
    return Authenticate(data).execute()

# Recurso que expone la funcionalidad detail user
@users_blueprint.route('/users/me', methods=['GET'])
def detail():
    data = request.headers
    return GetUserDetail(data).query()

# Recurso que expone la funcionalidad de callback para TrueNative
@users_blueprint.route('/users/native/callback', methods=['PATCH'])
def callback():
    data = request.get_json()
    return VerifyUser(data).execute()

# Recurso que expone la funcionalidad update user
@users_blueprint.route('/users/<string:userId>', methods=['PATCH'])
def update(userId):
    data = request.get_json()
    UpdateUser(userId, data).execute()
    return jsonify({'msg': 'el usuario ha sido actualizado'})

# Recurso que expone la funcionalidad de consulta de usuario po ID
@users_blueprint.route('/users/<string:userId>', methods=['GET'])
def get(userId):
    return GetUserById(userId).query()

# Recurso que expone la funcionalidad create user
@users_blueprint.route('/users', methods=['POST'])
def create():
    data = request.get_json()
    result = CreateUser(data).execute()
    verifyUserExternal(result.id, data, request.headers)
    return jsonify({'id': result.id, 'createdAt': formatDateTimeToUTC(str(result.createdAt))}), 201
from flask import request, Blueprint
from flask.json import jsonify
from commands.create_score import CreateScore
from commands.reset_scores import ResetScores
from queries.get_scores_by_post import GetScoresByPost
from queries.detail_score import DetailScore
from queries.get_scores import GetScores

scores_blueprint = Blueprint('scores', __name__)

# Recurso que expone la funcionalidad healthcheck
@scores_blueprint.route('/scores/ping', methods=['GET'])
def healthCheck():
    return "pong"

# Recurso que expone la funcionalidad reset utilidades
@scores_blueprint.route('/scores/reset', methods=['DELETE'])
def resetScores():
    ResetScores().execute()
    return jsonify({'msg': 'Todos los datos fueron eliminados'})

# Recurso que expone la funcionalidad de consulta de utilidad por publicación
@scores_blueprint.route('/scores/posts/<string:postId>', methods=['GET'])
def getScoresByPost(postId):
    return GetScoresByPost(postId).query()

# Recurso que expone la funcionalidad de consulta de utilidad por ID
@scores_blueprint.route('/scores/<string:id>', methods=['GET'])
def detailScore(id):
    return DetailScore(id).query()

# Recurso que expone la funcionalidad de consulta de utilidades
@scores_blueprint.route('/scores', methods=['GET'])
def getScores():
    return GetScores().query()

# Recurso que expone la funcionalidad creación de utilidad
@scores_blueprint.route('/scores', methods=['POST'])
def createScore():
    data = request.get_json()
    return CreateScore(data).execute(), 201
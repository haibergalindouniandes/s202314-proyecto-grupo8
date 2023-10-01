from flask import request, Blueprint
from flask.json import jsonify
from agregators.posts import agregator, getPostHealth
import traceback
from flask import abort, render_template, current_app
import logging
from errors.errors import  InvalidToken, MissingToken, NotFound


rf05_blueprint = Blueprint('rf005', __name__)


@rf05_blueprint.route('/rf005/posts/ping', methods=['GET'])
def postHealth():
    header = request.headers
    return getPostHealth(header)

@rf05_blueprint.route('/rf005/ping', methods=['GET'])
def health():
    return "pong"

@rf05_blueprint.route('/rf005/posts/<string:id>', methods=['GET'])
def getInfoPostById(id):
    try:
        header = request.headers
    #        user = validateToken(header)
        current_app.logger.info('Se realiza llamada al servicio agregator')
        result = agregator(id, header)        
        return jsonify(result), 200
#    except InvalidToken as e:  # pragma: no cover
#        return '', 401
#    except MissingToken as e:  # pragma: no cover
#        return '', 403
#    except IdNotUUID as e:
#        return '', 400
    except NotFound as e:
        return '', 404
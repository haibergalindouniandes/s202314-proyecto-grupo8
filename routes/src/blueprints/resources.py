from flask import request, Blueprint
from flask.json import jsonify
from commands.create import CreateRoute
from commands.query import QueryRoute
from commands.reset import ResetRoutes
from commands.get import GetRoute
from commands.delete import DeleteRoute
#from queries.detail import GetRouteDetail
from commands.update import UpdateRoute
from utilities.utilities import formatDateTimeToUTC
from validators.validators import validateToken, validateExistTokenHeader
import traceback
from errors.errors import ApiError,  FligthExists, ValidateDates, InvalidToken, MissingToken, validateFlightError,IdNotUUID,NotFound
from flask import abort, render_template, current_app

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/routes/ping', methods=['GET'])
def health():
    return "pong"

@routes_blueprint.route('/routes/reset', methods=['POST'])
def reset():
    ResetRoutes().execute()
    return jsonify({'msg': 'Todos los datos fueron eliminados'})


@routes_blueprint.route('/routes', methods=['POST'])
def create():  
    current_app.logger.info('CReacion*********')  
    header = request.headers
    current_app.logger.info('se asignan headers')
    validateExistTokenHeader(header)
    current_app.logger.info('pasa validacion de header')
    user = validateToken(header)
    current_app.logger.info('pasa validacion deusuario')
    data = request.get_json()
    current_app.logger.info('se asigna request')
    result = CreateRoute(data).execute()
    current_app.logger.info('se realizo creación antes de respuesta')
    return jsonify({'id': result.id, 'createdAt': formatDateTimeToUTC(str(result.createdAt))}), 201
    
@routes_blueprint.route('/routes', methods=['GET'])
def queryflightId():
    
    header = request.headers
    user = validateToken(header) 
    args = request.args
    flight =  args.get('flight')
    result = QueryRoute(flight).execute()
    return jsonify(result), 200
    


@routes_blueprint.route('/routes/<string:id>', methods=['GET'])
def getRouteId(id):
    try:
        header = request.headers
        user = validateToken(header)
        result = GetRoute(id).execute()
        return jsonify({'id': result.id,'flightId':result.flightId,'sourceAirportCode': result.sourceAirportCode, 'sourceCountry': result.sourceCountry, 'destinyAirportCode': result.destinyAirportCode, 'destinyCountry': result.destinyCountry, 'bagCost': result.bagCost, 'plannedStartDate': result.plannedStartDate,'plannedEndDate':result.plannedEndDate, 'createdAt':result.createdAt}), 200
    except InvalidToken as e:  # pragma: no cover
        return '', 401
    except MissingToken as e:  # pragma: no cover
        return '', 403
    except IdNotUUID as e:
        return '', 400
    except NotFound as e:
        return '', 404

@routes_blueprint.route('/routes/<string:id>', methods=['DELETE'])
def deleteRoute(id):
    try:
        header = request.headers
        user = validateToken(header)
        DeleteRoute(id).execute()
        return jsonify({'msg': 'el trayecto fue eliminado'}), 200
    except InvalidToken as e:  # pragma: no cover
        return '', 401
    except MissingToken as e:  # pragma: no cover
        return '', 403
    except IdNotUUID as e:
        return '', 400
    except NotFound as e:
        return '', 404
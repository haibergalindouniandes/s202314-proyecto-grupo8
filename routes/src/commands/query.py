# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError, validateFlightError  
from validators.validators import validateFlight
from models.models import db, Route
from sqlalchemy.exc import SQLAlchemyError
import uuid
import hashlib
import traceback
import json
from datetime import datetime
from flask import abort, render_template, current_app


def dict_helper(objlist):
    result2 = [item.obj_to_dict() for item in objlist]
    return result2

# Clase que contiene la logica de Consulta de rutas
class QueryRoute(BaseCommannd):
    def __init__(self, flightId):   
        current_app.logger.info('Inicia constructor de QueryRoute')     
        self.flightId = flightId

    # Función que realiza creación del usuario
    def execute(self):
        current_app.logger.info('Inicia ejecucion de QueryRoute')
        try:
            current_app.logger.info(self.flightId)
            if self.flightId is None:  
                current_app.logger.info('Entro validación si no existe valor en el flightId')              
                routeList = Route.query.all()
                current_app.logger.info('resultado consulta general')    
                current_app.logger.info(routeList)
            else:
                #validateFlight(self.flightId)
                current_app.logger.info('Flujo Else se consulta FlightId infgresado para ver si existe')    
                routeList = Route.query.filter(Route.flightId == self.flightId)
                current_app.logger.info('resultado flujo else flight id particular')
                current_app.logger.info(routeList)    
            
            current_app.logger.info('resultado con la conversion a diccionario')
            current_app.logger.info(dict_helper(routeList))
            return  dict_helper(routeList)
        except SQLAlchemyError as e:# pragma: no cover
            traceback.print_exc()
            raise ApiError(e)        
     
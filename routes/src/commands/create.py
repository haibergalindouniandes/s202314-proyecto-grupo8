# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError,  FligthExists, ValidateDates, InvalidToken
from validators.validators import validateSchema, createRouteSchema
from validators.validators_flightid import validateExistFligthId
from models.models import db, Route
from commands.query import QueryRoute
from sqlalchemy.exc import SQLAlchemyError
import uuid
import hashlib
import traceback
from datetime import datetime
import logging
from flask import abort, render_template, current_app

# Clase que contiene la logica de creción de rutas
class CreateRoute(BaseCommannd):
    def __init__(self, route):
        current_app.logger.info('Create ROute Constructor inicia validacion de request')
        self.validateRequest(route)

    # Función que valida si existe un usuario con el email
    def validateDates(self, plannedStartDate, plannedEndDate):
        current_app.logger.info('Inicia validacion de fechas')
        formatting = "%Y-%m-%dT%H:%M:%S.%fZ"
        date1 = datetime.strptime(plannedStartDate, formatting)
        date2 = datetime.strptime(plannedEndDate, formatting)
        actualDate = datetime.now()
        current_app.logger.info('Antes IF')
        if actualDate > date1:
            current_app.logger.info('Primer If se genera Error')
            raise ValidateDates  # pragma: no cover
        elif date1 > date2:
            current_app.logger.info('segundo If se genera Error')
            raise ValidateDates  # pragma: no cover
        elif date1 == date2:
            current_app.logger.info('tercer If se genera Error')
            raise ValidateDates  # pragma: no cover        
        
        
        current_app.logger.info('antes de retornar true')
        return True
        
    
    #Funcion para vlaidar si existe un fligthID
    #def existFligthId(self):
    #    result = QueryRoute(self.flightId).execute()
    #    if result is None:
    #        raise fligthExists 

    # Función que valida el request del servicio
    def validateRequest(self, routeJson):
        # Validacion del request
        current_app.logger.info('Inicia metodo validacion de rquest')
        validateSchema(routeJson, createRouteSchema)
        current_app.logger.info('se paso la validación de schema')
        # Asignacion de variables
        self.flightId = routeJson['flightId']        
        self.sourceAirportCode = routeJson['sourceAirportCode']
        self.sourceCountry = routeJson['sourceCountry']
        self.destinyAirportCode = routeJson['destinyAirportCode']
        self.destinyCountry = routeJson['destinyCountry']
        self.bagCost = routeJson['bagCost']
        self.plannedStartDate = routeJson['plannedStartDate']
        self.plannedEndDate = routeJson['plannedEndDate']
        current_app.logger.info('se finalizo la asignación')
        
        self.validateDates(self.plannedStartDate, self.plannedEndDate)
        current_app.logger.info('se finalizo validacion de fechas')        
        if validateExistFligthId(self.flightId):
            current_app.logger.info('se genera error porque el  vuelo ya existe')
            raise FligthExists
        
        current_app.logger.info('se finalizo validacion de validateExistFligthId')
        
        

    # Función que realiza creación del usuario
    def execute(self):            
        current_app.logger.info('paso ejecucion')
        newRoute = Route(
            flightId=self.flightId,
            sourceAirportCode=self.sourceAirportCode,
            sourceCountry=self.sourceCountry,
            destinyAirportCode=self.destinyAirportCode,
            destinyCountry=self.destinyCountry,
            bagCost=self.bagCost,
            plannedStartDate=self.plannedStartDate,
            plannedEndDate=self.plannedEndDate,
            )
        db.session.add(newRoute)
        db.session.commit()
        current_app.logger.info('se creo trayecto')
        return newRoute
        
     
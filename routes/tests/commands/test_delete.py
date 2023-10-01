import random
from src.commands.create import CreateRoute
from src.commands.delete import DeleteRoute
from faker import Faker
from faker.providers import DynamicProvider
import json


# Clase que contiene la logica de las pruebas del servicio de eliminiacion de trayectos
class TestQuery():
    
    flightId_values_provider = DynamicProvider(
        provider_name="flightId_provider",
        elements=[ "889", "890","886", "887", "888"],
        )
    
    sourceAirportCode_values_provider = DynamicProvider(
        provider_name="sourceAirportCode_provider",
        elements=["BOG", "MDE", "AXM", "BGA", "LET","PEI","ADZ","SMR"],
        )
    
    sourceCountry_values_provider = DynamicProvider(
        provider_name="sourceCountry_provider",
        elements=["Colombia", "Mexico", "Peru", "Ecuador", "Brasil","EEUU","España","Noruega"],
        )
    
    dataFactory = Faker()
    dataFactory.add_provider(flightId_values_provider)
    dataFactory.add_provider(sourceAirportCode_values_provider)
    dataFactory.add_provider(sourceCountry_values_provider)    
    
    flightId = None
    sourceAirportCode = None
    sourceCountry = None
    destinyAirportCode = None
    destinyCountry = None
    bagCost = None
    plannedStartDate = None
    plannedEndDate = None
    data = {}
    
    # Función que genera datos del la ruta
    def set_up(self):         
        self.flightId = self.dataFactory.flightId_provider()
        self.sourceAirportCode = self.dataFactory.sourceAirportCode_provider()
        self.sourceCountry = self.dataFactory.sourceCountry_provider()
        self.destinyAirportCode = self.dataFactory.sourceAirportCode_provider()
        self.destinyCountry = self.dataFactory.sourceCountry_provider()
        self.bagCost = self.dataFactory.pydecimal(left_digits=3, right_digits=0, positive=True)
        self.plannedStartDate = '2023-09-01T21:20:53.214Z'
        self.plannedEndDate = '2023-09-27T21:20:53.214Z'
        
        self.data = {
            "flightId":f"{self.flightId}",
            "sourceAirportCode":f"{self.sourceAirportCode}",
            "sourceCountry":f"{self.sourceCountry}",
            "destinyAirportCode":f"{self.destinyAirportCode}",
            "destinyCountry":f"{self.destinyCountry}",
            "bagCost": int(self.bagCost),
            "plannedStartDate":f"{self.plannedStartDate}",
            "plannedEndDate":f"{self.plannedEndDate}"
        }
        
    # Función que valida la eliminacion exitosa de una ruta
    def test_delete_route(self):
        # Creación trayecyo
        self.set_up()
        result1 = CreateRoute(self.data).execute()
        print(result1.id)
        result2 = DeleteRoute(result1.id).execute()
        print(result2)
        assert result2 == None
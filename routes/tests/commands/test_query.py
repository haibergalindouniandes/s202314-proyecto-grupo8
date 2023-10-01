import random
from src.commands.query import QueryRoute
from faker import Faker
from faker.providers import DynamicProvider

# Clase que contiene la logica de las pruebas del servicio de consulta de trayectos
class TestQuery():
    
    flightId_values_provider = DynamicProvider(
        provider_name="flightId_provider",
        elements=["686", "687", "688", "689", "690"],
        )
    dataFactory = Faker()
    dataFactory.add_provider(flightId_values_provider)
    
    flightId = None
    
    
    # Función que genera datos del la ruta
    def set_up(self): 
        
        self.flightId = self.dataFactory.flightId_provider()
        
    # consulta de una ruta
    def test_create_get_route(self):
        # consulta de una ruta
        self.set_up()
        result = QueryRoute(self.flightId).execute()
        assert result != None
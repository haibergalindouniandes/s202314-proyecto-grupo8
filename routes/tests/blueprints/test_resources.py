import random
from src.main import app
from faker import Faker
import json

# Clase que contiene la logica del test
class TestResources():

    # Función que valida el estado del servidor
    def test_health_check(self):
        # Salud microservicio de oferta
        with app.test_client() as test_client:
            response = test_client.get(
                '/routes/ping'
            )
            data = str(response.data)
        assert response.status_code == 200
        assert 'pong' in data

    # Función que valida el estado del servidor
    def test_reset_check(self):
        # Reset tabla ofertas
        with app.test_client() as test_client:
            response = test_client.post(
                '/routes/reset'
            )
        assert response.status_code == 200
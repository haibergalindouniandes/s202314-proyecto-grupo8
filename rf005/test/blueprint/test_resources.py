from src.main import app
from faker import Faker
from datetime import datetime, timedelta

from test.mocks import ( 
    mock_post_rf005_success,
    mock_post_users_success,
    mock_post_route_success,
    mock_post_offers_success,
    mock_post_scores_success
)
from faker.providers import DynamicProvider
from httmock import HTTMock
from uuid import uuid4




# Clase que contiene la logica del test
class TestRF005Resources:




    def test_rf005_success(self):
        # Verificacion de Happy Path        
        with app.test_client() as test_client:
            with HTTMock(                               
                mock_post_rf005_success,
                mock_post_users_success,
                mock_post_route_success,
                mock_post_offers_success,
                mock_post_scores_success
            ):
                response = test_client.get(
                    "/rf005/posts/7db2089e-51e7-11ee-a25b-0242ac120005"                   
                )
        assert response.status_code == 200
        
    
    # Funciones de pruebas de RF005
    def test_health_check(self):
        # Salud microservicio de rf005
        with app.test_client() as test_client:
            response = test_client.get("/rf005/ping")
            data = str(response.data)
        assert response.status_code == 200
        assert "pong" in data
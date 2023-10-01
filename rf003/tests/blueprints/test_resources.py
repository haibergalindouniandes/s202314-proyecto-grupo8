from src.main import app
from faker import Faker
from datetime import datetime, timedelta
from tests.mocks import (
    mock_failed_auth,
    mock_success_auth,
    mock_forbidden_auth,
    mock_query_route_empty,
    mock_user_post_route_success,
    mock_post_route_error,
    mock_post_route_success,
    mock_post_create_success,
)
from faker.providers import DynamicProvider
from httmock import HTTMock
from uuid import uuid4
import json

# Clase que contiene la logica del test
class TestRF003Resources:

    flightId_values_provider = DynamicProvider(
        provider_name="flightId_provider",
        elements=["889", "890", "886", "887", "888"],
    )

    sourceAirportCode_values_provider = DynamicProvider(
        provider_name="sourceAirportCode_provider",
        elements=["BOG", "MDE", "AXM", "BGA", "LET", "PEI", "ADZ", "SMR"],
    )

    sourceCountry_values_provider = DynamicProvider(
        provider_name="sourceCountry_provider",
        elements=[
            "Colombia",
            "Mexico",
            "Peru",
            "Ecuador",
            "Brasil",
            "EEUU",
            "España",
            "Noruega",
        ],
    )

    # Declaración constantes
    dataFactory = Faker()
    dataFactory.add_provider(flightId_values_provider)
    dataFactory.add_provider(sourceAirportCode_values_provider)
    dataFactory.add_provider(sourceCountry_values_provider)

    flightId = None
    expireAt = None
    plannedStartDate = None
    plannedEndDate = None
    origin_airportCode = None
    origin_country = None
    destiny_airportCode = None
    destiny_country = None
    bagCost = None
    data = {}

    # Funciones que generan datos para las pruebas de RF003
    def set_up_working(self):
        self.flightId = self.dataFactory.uuid4()
        self.expireAt = f"{str(datetime.today() + timedelta(days=1)).split('.')[0].replace(' ', 'T')}.214Z"
        self.plannedStartDate = f"{str(datetime.today() + timedelta(days=1)).split('.')[0].replace(' ', 'T')}.214Z"
        self.plannedEndDate = f"{str(datetime.today() + timedelta(days=10)).split('.')[0].replace(' ', 'T')}.214Z"
        self.origin_airportCode = self.dataFactory.sourceAirportCode_provider()
        self.origin_country = self.dataFactory.sourceCountry_provider()
        self.destiny_airportCode = self.dataFactory.sourceAirportCode_provider()
        self.destiny_country = self.dataFactory.sourceCountry_provider()
        self.bagCost = self.dataFactory.pydecimal(
            left_digits=4, right_digits=0, positive=True
        )
        self.data = {
            "flightId": self.flightId,
            "expireAt": self.expireAt,
            "plannedStartDate": self.plannedStartDate,
            "plannedEndDate": self.plannedEndDate,
            "origin": {
                "airportCode": self.origin_airportCode,
                "country": self.origin_country,
            },
            "destiny": {
                "airportCode": self.destiny_airportCode,
                "country": self.destiny_country,
            },
            "bagCost": int(self.bagCost),
        }

    def set_up_missing(self):
        self.flightId = self.dataFactory.uuid4()
        self.expireAt = (
            (datetime.now() + timedelta(days=self.dataFactory.random_int(1, 30)))
            .replace(microsecond=0)
            .isoformat()
        )
        self.plannedStartDate = f"{str(datetime.today() + timedelta(days=1)).split('.')[0].replace(' ', 'T')}.214Z"
        self.plannedEndDate = f"{str(datetime.today() + timedelta(days=10)).split('.')[0].replace(' ', 'T')}.214Z"
        self.origin_airportCode = self.dataFactory.sourceAirportCode_provider()
        self.origin_country = self.dataFactory.sourceCountry_provider()
        self.destiny_airportCode = self.dataFactory.sourceAirportCode_provider()
        self.destiny_country = self.dataFactory.sourceCountry_provider()
        self.data_missing = {
            "flightId": self.flightId,
            "expireAt": self.expireAt,
            "plannedStartDate": self.plannedStartDate,
            "plannedEndDate": self.plannedEndDate,
            "origin": {
                "airportCode": self.origin_airportCode,
                "country": self.origin_country,
            },
            "destiny": {
                "airportCode": self.destiny_airportCode,
                "country": self.destiny_country,
            },
        }

    # Funciones de pruebas de RF003
    def test_health_check(self):
        # Salud microservicio de rf003
        with app.test_client() as test_client:
            response = test_client.get("/rf003/ping")
            data = str(response.data)
        assert response.status_code == 200
        assert "pong" in data

    def test_rf003_token(self):
        # Verificacion de Token
        self.set_up_working()
        with app.test_client() as test_client:
            with HTTMock(mock_failed_auth):
                response = test_client.post(
                    "/rf003/posts",
                    json=self.data,
                    headers={"Authorization": f"Bearer {uuid4()}"},
                )
        assert response.status_code == 401

    def test_rf003_token_2(self):
        # Verificacion de Token
        self.set_up_working()
        with app.test_client() as test_client:
            with HTTMock(mock_forbidden_auth):
                response = test_client.post(
                    "/rf003/posts",
                    json=self.data,
                    headers={"Authorization": f"Bearer {uuid4()}"},
                )
        assert response.status_code == 403

    def test_rf003_schema(self):
        # Verificacion de Schema
        self.set_up_missing()
        with app.test_client() as test_client:
            with HTTMock(mock_success_auth):
                response = test_client.post(
                    "/rf003/posts",
                    json=self.data_missing,
                    headers={"Authorization": f"Bearer {uuid4()}"},
                )
        assert response.status_code == 400

    def test_rf003_route_date_error(self):
        # Verificacion de error 412
        self.set_up_working()
        with app.test_client() as test_client:
            with HTTMock(
                mock_success_auth,
                mock_query_route_empty,
                mock_user_post_route_success,
                mock_post_route_error,
            ):
                response = test_client.post(
                    "/rf003/posts",
                    json=self.data,
                    headers={"Authorization": f"Bearer {uuid4()}"},
                )
        assert response.status_code == 412

    def test_rf003_success(self):
        # Verificacion de Happy Path
        self.set_up_working()
        with app.test_client() as test_client:
            with HTTMock(
                mock_success_auth,
                mock_query_route_empty,
                mock_user_post_route_success,
                mock_post_route_success,
                mock_post_create_success,
            ):
                response = test_client.post(
                    "/rf003/posts",
                    json=self.data,
                    headers={"Authorization": f"Bearer {uuid4()}"},
                )
        assert response.status_code == 201

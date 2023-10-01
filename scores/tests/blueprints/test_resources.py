
from src.errors.errors import ScoresNotFound
from src.errors.errors import BadRequest
from src.main import app
from faker import Faker
import random
import uuid
import json

# Clase que contiene la logica del test
class TestResources():

    # Declaración constantes
    dataFactory = Faker()
    packageDescription = None
    packageSize = None
    packageAmount = None
    isPackageFragile = None
    offerAmount = None
    offerId = None
    postId = None
    userId = None
    scoreId = None
    responseCreateScore = None
    data = {}  

    # Función que genera data de la utilidad
    def set_up(self):
        sizesTypes =  ["LARGE", "MEDIUM", "SMALL"]
        fragilTypes =  [True, False]
        self.packageDescription = self.dataFactory.text()
        self.packageSize = random.choice(sizesTypes)
        self.packageAmount = round(random.uniform(10, 30), 2)
        self.isPackageFragile = random.choice(fragilTypes)
        self.offerAmount = round(random.uniform(30.5, 50), 2)
        self.offerId = str(uuid.uuid4())
        self.postId = str(uuid.uuid4())
        self.userId = str(uuid.uuid4())
        self.scoreId = str(uuid.uuid4())
        
        self.data = {
            "packageDescription": f"{self.packageDescription}",
            "packageSize": f"{self.packageSize}",
            "packageAmount" : f"{self.packageAmount}",
            "isPackageFragile" : self.isPackageFragile,
            "offerAmount": f"{self.offerAmount}",
            "offerId": f"{self.offerId}",
            "postId": f"{self.postId}",
            "userId": f"{self.userId}"
        }

    # Función hace el llamado al recurso de creacion de utilidad
    def execute_create_score(self, data):
        with app.test_client() as test_client:
            self.responseCreateScore = test_client.post(
                '/scores', json=json.dumps(data)
            )

    # Función que valida la creación exitosa de una utilidad con un request invalido
    def validate_bad_request_create_score(self): 
        response_json = json.loads(self.responseCreateScore.data)   
        assert self.responseCreateScore.status_code == BadRequest.code
        assert 'msg' in response_json
        assert response_json['msg'] == BadRequest.description

    # Función que valida la creación exitosa de una utilidad con un request invalido
    def validate_score_not_found(self, response): 
        response_json = json.loads(response.data)   
        assert response.status_code == ScoresNotFound.code
        assert 'msg' in response_json
        assert response_json['msg'] == ScoresNotFound.description        

    # Función que valida el estado del servidor
    def test_health_check(self):
        with app.test_client() as test_client:
            response = test_client.get(
                '/scores/ping'
            )
            data = str(response.data)
        assert response.status_code == 200
        assert 'pong' in data

   # Función que limpia todos los registros de la tabla scores
    def test_reset_scores(self):
        # Reset tabla scores
        with app.test_client() as test_client:
            response = test_client.delete(
                '/scores/reset'
            )
            response_json = json.loads(response.data)
        assert response.status_code == 200
        assert 'msg' in response_json
        assert response_json['msg'] == 'Todos los datos fueron eliminados'

    # Función que valida la creación fallida de una utilidad
    def test_create_score_bad_request(self):
        self.set_up()
        # Creación nuevo score con request invalido
        self.execute_create_score(self.data)
        self.validate_bad_request_create_score()

    # Función que valida la consulta de una utilidad por el ID y no existe
    def test_get_score_non_existent(self):
        self.set_up()
        # Consulta de score
        with app.test_client() as test_client:
            response = test_client.get(
                f'/scores/{self.scoreId}'
            )
        self.validate_score_not_found(response)

    # Función que valida la consulta de una utilidad por el postId y no existe
    def test_get_score_postid_non_existent(self):
        self.set_up()
        # Consulta de score
        with app.test_client() as test_client:
            response = test_client.get(
                f'/scores/posts/{self.scoreId}'
            )
        self.validate_score_not_found(response)        

    # Función que valida que se genere el error Not Found 
    def test_get_scores_not_found(self):
        self.set_up()
        # Consulta de scores
        with app.test_client() as test_client:
            response = test_client.get(
                f'/scores'
            )
        self.validate_score_not_found(response)        
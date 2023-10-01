import random
import uuid
import src.main
from src.queries.detail_score import DetailScore
from src.commands.create_score import CreateScore
from faker import Faker

# Clase que contiene la logica de las pruebas del servicio
class TestDetailScore():
    
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
        
    # Función que crea una utilidad
    def create_score(self):    
        # Creación nueva utilidad
        self.set_up()
        result = CreateScore(self.data).execute()
        self.scoreId = result["id"]

    # Función que consulta exitosamente el detalle de una utilidad
    def test_detail_score(self):
        # Creación nuevo usuario
        self.set_up()
        self.create_score()
        # Consulta de utilidad
        scoreDetail = DetailScore(self.scoreId).query()
        assert scoreDetail["id"] == self.scoreId
        assert scoreDetail["packageDescription"]  == self.packageDescription
        assert scoreDetail["packageSize"]  == self.packageSize
        assert "packageAmount" in scoreDetail
        assert scoreDetail["isPackageFragile"]  == self.isPackageFragile
        assert "score" in scoreDetail
        assert "offerAmount" in scoreDetail
        assert scoreDetail["offerId"]  == str(self.offerId)
        assert scoreDetail["postId"]  == str(self.postId)
        assert scoreDetail["userId"]  == str(self.userId)
        assert "createdAt" in scoreDetail
        
    # Función que valida la consulta de una utilidad con un Id invalido
    def test_detail_score_invalid_id(self):
        try:
            # Consulta de usuario
            DetailScore(f"{self.scoreId}wrong").query()
        except Exception as e:
            assert e.code == 400
            assert e.description == "El ID ingresado es invalido"
            
    # Función que valida la consulta de una utilidad con un Id no existente
    def test_detail_score_with_non_existent_id(self):
        try:
            # Consulta de usuario
            DetailScore(str(uuid.uuid4())).query()
        except Exception as e:
            assert e.code == 404
            assert e.description == "No se encontraron datos"
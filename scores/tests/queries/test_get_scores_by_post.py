import random
import uuid
import src.main
from src.queries.get_scores_by_post import GetScoresByPost
from src.commands.create_score import CreateScore
from faker import Faker

# Clase que contiene la logica de las pruebas del servicio
class TestGetScoresByPost():
    
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
        CreateScore(self.data).execute()

    # Función que consulta exitosamente el listado utilidades de una publicación
    def test_get_score_by_post(self):
        # Creación nuevo usuario
        self.set_up()
        self.create_score()
        # Consulta de utilidad
        scoreDetail = GetScoresByPost(str(self.postId)).query()
        assert "id" in scoreDetail[0]
        assert "packageDescription" in scoreDetail[0]
        assert "packageSize" in scoreDetail[0]
        assert "packageAmount" in scoreDetail[0]
        assert "isPackageFragile" in scoreDetail[0]
        assert "score" in scoreDetail[0]
        assert "offerAmount" in scoreDetail[0]
        assert "offerId" in scoreDetail[0]
        assert "userId" in scoreDetail[0]
        assert "createdAt" in scoreDetail[0]
        assert scoreDetail[0]["postId"]  == str(self.postId)
        
        
    # Función que valida la consulta de una utilidad con un Id de publicacion invalido
    def test_get_score_by_invalid_post(self):
        try:
            # Consulta de usuario
            GetScoresByPost(f"{self.postId}wrong").query()
        except Exception as e:
            assert e.code == 400
            assert e.description == "El ID ingresado es invalido"
            
    # Función que valida la consulta de una utilidad con un Id de publicacion no existente
    def test_get_score_with_non_existent_post(self):
        try:
            # Consulta de usuario
            GetScoresByPost(str(uuid.uuid4())).query()
        except Exception as e:
            assert e.code == 404
            assert e.description == "No se encontraron datos"
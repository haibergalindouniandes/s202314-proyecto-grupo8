import random
import uuid
import src.main
from src.queries.get_scores import GetScores
from src.commands.reset_scores import ResetScores
from src.commands.create_score import CreateScore
from faker import Faker

# Clase que contiene la logica de las pruebas del servicio
class TestGetScores():
    
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
    scoresToCreate = 3

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
    def create_scores(self):    
        # Creación utilidades
        self.set_up()
        for item in range(3):
            CreateScore(self.data).execute()

    # Función que consulta exitosamente el listado utilidades
    def test_get_scores(self):
        # Creación nuevo usuario
        self.set_up()
        self.create_scores()
        # Consulta de utilidad
        scoreDetail = GetScores().query()
        assert "id" in scoreDetail[0]
        assert "packageDescription" in scoreDetail[0]
        assert "packageSize" in scoreDetail[0]
        assert "packageAmount" in scoreDetail[0]
        assert "isPackageFragile" in scoreDetail[0]
        assert "score" in scoreDetail[0]
        assert "offerAmount" in scoreDetail[0]
        assert "postId" in scoreDetail[0]
        assert "offerId" in scoreDetail[0]
        assert "userId" in scoreDetail[0]
        assert "createdAt" in scoreDetail[0]
        assert len(scoreDetail) == (self.scoresToCreate + 1)
        
        
    # Función que valida la respuesta cuando no hay utilidades registradas
    def test_get_scores_not_found(self):
        try:
            # Limpieza tabla scores
            ResetScores().execute()
            # Consulta de usuario
            GetScores().query()
        except Exception as e:
            assert e.code == 404
            assert e.description == "No se encontraron datos"
            
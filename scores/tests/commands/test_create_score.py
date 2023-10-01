import random
import uuid
import src.main
from src.commands.create_score import CreateScore
from faker import Faker

# Clase que contiene la logica de las pruebas del servicio
class TestCreateScore():
    
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
            
    # Función que valida la creación exitosa de una utilidad
    def test_create_new_score(self):
        # Creación usuario
        self.set_up()
        result = CreateScore(self.data).execute()
        assert result != None
    
    # Función que valida la creación de una utilidad cuando se envia un request invalido
    def test_create_score_bad_request(self):
        try:
            # Creación usuario
            self.set_up()
            self.data["packageSize"] = "EXTRA_LARGE"
            self.data["postId"] = f"{self.postId}wrong"
            self.data["userId"] = f"{self.userId}wrong"
            # Creación usuario con data incompleta
            CreateScore(self.data).execute()
        except Exception as e:
            assert e.code == 400        
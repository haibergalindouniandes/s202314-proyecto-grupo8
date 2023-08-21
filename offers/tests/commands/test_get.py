import random
from src.commands.create import CreateOffer
from src.commands.get import GetOffer
from faker import Faker
import uuid

# Clase que contiene la logica de las pruebas del servicio
class TestCreate():

    # Declaración constantes
    sizeList = ["LARGE", "MEDIUM", "SMALL"]
    dataFactory = Faker()
    offerId = None
    postId = None
    userId = None
    description = None
    size = None
    fragile = None
    offer = None
    data = {}

    # Función que genera datos del la oferta
    def set_up(self):
        self.postId = self.dataFactory.uuid4()
        self.userId = self.dataFactory.uuid4()
        self.description = self.dataFactory.sentence(nb_words=8)
        self.size = random.choice(self.sizeList)
        self.fragile = random.choice([True, False])
        self.offer = self.dataFactory.pydecimal(left_digits=6, right_digits=2, positive=True)
        self.data = {
            "postId": f"{self.postId}",
            "description": f"{self.description}",
            "size": f"{self.size}",
            "fragile": self.fragile,
            "offer": self.offer
        }

    # Función que valida la creación exitosa de una oferta
    def create_offer(self):
        result = CreateOffer(self.data, self.userId).execute()
        assert result != None
        self.offerId = result.id

    # Función que valida retorno de la oferta dada
    def test_get_offer(self):
        # Creación nueva oferta
        self.set_up()
        self.create_offer()
        result = GetOffer(self.offerId).execute()
        assert result != None

    # Función que valida obtener de una oferta que no existe
    def test_get_offer_missing(self):
        try:
            # Crear ID no existente
            offerId = uuid.uuid4()
            GetOffer(offerId).execute()
        except Exception as e:
            assert e.code == 404

    # Función que valida obtener de una oferta con ID incorrecto
    def test_get_offer_wrong_id(self):
        try:
            # Crear ID no existente
            offerId = "12"
            GetOffer(offerId).execute()
        except Exception as e:
            assert e.code == 400
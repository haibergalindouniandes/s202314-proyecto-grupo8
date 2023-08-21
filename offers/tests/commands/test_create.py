import random
from src.commands.create import CreateOffer
from faker import Faker

# Clase que contiene la logica de las pruebas del servicio
class TestCreate():

    # Declaración constantes
    sizeList = ["LARGE", "MEDIUM", "SMALL"]
    dataFactory = Faker()
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
    def test_create_new_offer(self):
        # Creación oferta
        self.set_up()
        result = CreateOffer(self.data, self.userId).execute()
        assert result != None

    # Función que valida la creación de una oferta con un parametro faltante
    def test_create_new_offer_missing(self):
        try:
            # Creación oferta
            self.set_up()
            data2 = {
            "postId": f"{self.postId}",
            "description": f"{self.description}",
            "size": f"{self.size}",
            "fragile": self.fragile
        }
            CreateOffer(data2, self.userId).execute()
        except Exception as e:
            assert e.code == 400

    # Función que valida la creación de una oferta con un parametro mal
    def test_create_new_offer_wrong(self):
        try:
            # Creación oferta
            self.set_up()
            data3 = {
            "postId": f"{self.postId}",
            "description": f"{self.description}",
            "size": f"{self.size}",
            "fragile": self.fragile,
            "offer": -100
        }
            CreateOffer(data3, self.userId).execute()
        except Exception as e:
            assert e.code == 412
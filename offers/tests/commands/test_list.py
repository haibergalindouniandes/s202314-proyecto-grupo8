import random
from src.commands.create import CreateOffer
from src.commands.list import ListOffer
from faker import Faker
import uuid

# Clase que contiene la logica de las pruebas del servicio
class TestCreate():

    # Declaración constantes
    sizeList = ["LARGE", "MEDIUM", "SMALL"]
    dataFactory = Faker()
    post = None
    owner = None
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
        self.owner = result.userId
        self.post = result.postId

    # Función que valida filtrado de la oferta sin parametros
    def test_list_offer(self):
        # Creación nueva oferta
        self.set_up()
        self.create_offer()
        result = ListOffer(None,None).execute()
        assert result != None

    # Función que valida filtrado de la oferta solo con post
    def test_list_offer_only_post(self):
        # Creación nueva oferta
        self.set_up()
        self.create_offer()
        result = ListOffer(self.post,None).execute()
        assert result != None

    # Función que valida filtrado de la oferta solo con owner
    def test_list_offer_only_owner(self):
        # Creación nueva oferta
        self.set_up()
        self.create_offer()
        result = ListOffer(None,self.owner).execute()
        assert result != None

    # Función que valida filtrado de la oferta con dos parametros
    def test_list_offer_both(self):
        # Creación nueva oferta
        self.set_up()
        self.create_offer()
        result = ListOffer(self.post,self.owner).execute()
        assert result != None

    # Función que valida obtener de una oferta con post ID incorrecto
    def test_list_offer_wrong_id_post(self):
        try:
            # Crear ID no existente
            post = "12"
            ListOffer(post,None).execute()
        except Exception as e:
            assert e.code == 400

    # Función que valida obtener de una oferta con owner ID incorrecto
    def test_list_offer_wrong_id_post(self):
        try:
            # Crear ID no existente
            owner = "12"
            ListOffer(None,owner).execute()
        except Exception as e:
            assert e.code == 400

    # Función que valida obtener de una oferta con ambos ID incorrecto
    def test_list_offer_wrong_id_post(self):
        try:
            # Crear ID no existente
            owner = "12"
            post = "15"
            ListOffer(post,owner).execute()
        except Exception as e:
            assert e.code == 400
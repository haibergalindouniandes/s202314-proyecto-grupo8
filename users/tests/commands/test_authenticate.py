from faker import Faker
from src.commands.create import CreateUser
from src.commands.authenticate import Authenticate
import uuid

# Clase que contiene la logica de las pruebas del servicio
class TestAuthenticate():
    
    # Declaración constantes
    dataFactory = Faker()
    userId = None
    username = None
    password = None
    email = None
    dni = None
    fullName = None
    phoneNumber = None
    data = {}    

    # Función que genera data del usuario
    def set_up(self):
        self.username = self.dataFactory.first_name() + str(self.dataFactory.random_int(1, 1000000))
        self.password = self.dataFactory.password(
            length=10, special_chars=False, upper_case=True, lower_case=True, digits=True)
        self.email = self.dataFactory.email()
        self.dni = str(self.dataFactory.random_int(1000, 100000000))
        self.fullName = self.dataFactory.name()
        self.phoneNumber = str(self.dataFactory.random_int(1000000, 100000000000))
        self.data = {
            "username": f"{self.username}",
            "password": f"{self.password}",
            "email": f"{self.email}",
            "dni": f"{self.dni}",
            "fullName": f"{self.fullName}",
            "phoneNumber": f"{self.phoneNumber}"
        }
        
    # Función que crea un usuario nuevo
    def create_user(self):    
        # Creación nuevo usuario
        result = CreateUser(self.data).execute()
        assert result != None
        self.userId = result.id
    
    # Función que valida la generación exitosa del token
    def test_generate_token(self):
        # Creación nuevo usuario
        self.set_up()
        self.create_user()
        # Generación token
        data = {
            "username": f"{self.username}",
            "password": f"{self.password}"
        }
        resultUpdate = Authenticate(data).execute()
        assert resultUpdate.id == self.userId
        assert resultUpdate.expireAt != None
        assert resultUpdate.token != None
        assert uuid.UUID(resultUpdate.token, version=4)

    # Función que valida la generación del token con credenciales erroneas
    def test_generate_token_wrong_credentials(self):
        try:
            # Creación nuevo usuario
            self.set_up()
            self.create_user()
            # Generación token
            data = {
                "username": f"{self.username}",
                "password": f"{self.password}wrong"
            }
            Authenticate(data).execute()
        except Exception as e:
            assert e.code == 404   

    # Función que valida la generación del token con un request invalido
    def test_generate_token_bad_request(self):
        try:
            # Creación nuevo usuario
            self.set_up()
            self.create_user()
            # Generación token
            data = {
                "username": f"{self.username}"
            }
            Authenticate(data).execute()
        except Exception as e:
            assert e.code == 400    

    # Función que valida la generación del token con un usuario no existente
    def test_generate_token_user_non_existent(self):
        try:
            # Generación token
            self.set_up()
            data = {
                "username": f"{self.username}",
                "password": f"{self.password}"
            }
            Authenticate(data).execute()
        except Exception as e:
            assert e.code == 404  
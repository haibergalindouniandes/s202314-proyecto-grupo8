from faker import Faker
from src.commands.create import CreateUser
from src.commands.update import UpdateUser
import uuid

# Clase que contiene la logica de las pruebas del servicio
class TestUpdate():
    
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
    
    # Función que valida la actualización exitosa de un usuario
    def test_update_user(self):
        # Creación nuevo usuario
        self.set_up()
        self.create_user()
        # Actualización información del usuario
        userId = self.userId
        self.set_up()
        status = "VERIFICADO"
        dataUpdate = {
            "status": f"{status}",
            "dni": f"{self.dni}",
            "fullName": f"{self.fullName}",
            "phoneNumber": f"{self.phoneNumber}"
        }
        resultUpdate = UpdateUser(userId, dataUpdate).execute()
        assert resultUpdate.status == status
        assert resultUpdate.dni == self.dni
        assert resultUpdate.fullName == self.fullName
        assert resultUpdate.phoneNumber == self.phoneNumber

    # Función que valida el request vacio
    def test_update_user_empty_request(self):
        try:
            # Creación nuevo usuario
            self.set_up()
            self.create_user()
            # Actualización información del usuario
            dataUpdate = {}
            UpdateUser(self.userId, dataUpdate).execute()
        except Exception as e:
            assert e.code == 400       

    # Función que valida los parametros de entrada
    def test_update_user_bad_request(self):
        try:
            # Creación nuevo usuario
            self.set_up()
            self.create_user()
            # Actualización información del usuario
            userId = self.userId
            self.set_up()
            dataUpdate = {
                "email": f"{self.email}"
            }
            UpdateUser(userId, dataUpdate).execute()
        except Exception as e:
            assert e.code == 400       

    # Función que valida la actualizacion de un usuario no registrado
    def test_update_user_non_existent(self):
        try:
            # Actualización información del usuario
            self.set_up()
            userId = uuid.uuid4()
            UpdateUser(userId, self.data).execute()
        except Exception as e:
            assert e.code == 404        
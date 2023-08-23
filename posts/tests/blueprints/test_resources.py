import uuid
from src.main import app
from faker import Faker
import json

# Clase que contiene la logica del test
class TestResources():

    # Declaración constantes
    dataFactory = Faker()
    userId = None
    username = None
    password = None
    email = None
    dni = None
    fullName = None
    phoneNumber = None
    token = None
    responseCreateUser = {}
    responseUpdateUser = {}
    responseDetailUser = {}
    responseToken = {}
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

    # Función que crea un usuario
    def execute_create_user(self, data):
        with app.test_client() as test_client:
            self.responseCreateUser = test_client.post(
                '/users', json=data
            )

    # Función que genera el token
    def execute_generate_token(self, data):
        with app.test_client() as test_client:
            self.responseToken = test_client.post(
                '/users/auth', json=data
            )

    # Función que consulta el detalle de un usuario
    def execute_detail_user(self, headers):
        with app.test_client() as test_client:
            self.responseDetailUser = test_client.get(
                '/users/me', headers=headers
            )

    # Función que crea un usuario exitosamente
    def create_user_success(self):
        # Creación nuevo usuario
        self.set_up()
        self.execute_create_user(self.data)
        self.validate_success_create_user()
        response_json = json.loads(self.responseCreateUser.data)
        self.userId = response_json['id']

    # Función que crea un usuario nuevo y genera el token exitosamente
    def create_user_generate_token_success(self):
        # Creación nuevo usuario
        self.create_user_success()
        # Generación token
        self.generate_token_success()
    
    # Función que actualiza un usuario
    def update_user(self, userId, data):
        dataUpdate = {}
        status= "VERIFICADO"
        if data == None:
            dataUpdate = {
                "status": f"{status}",
                "dni": f"{self.dni}",
                "fullName": f"{self.fullName}",
                "phoneNumber": f"{self.phoneNumber}"
            }
        else:
            dataUpdate = data
            
        with app.test_client() as test_client:
            self.responseUpdateUser = test_client.patch(
                f'/users/{userId}', json=dataUpdate
            )    
   
    # Función que genera el token exitosamente
    def generate_token_success(self):
        # Generación token
        dataAuthenticate = {
            "username": f"{self.username}",
            "password": f"{self.password}"
        }
        self.execute_generate_token(dataAuthenticate)
        self.validate_success_generate_token()   
    
    # Función que valida la creación exitosa de un usuario
    def validate_success_create_user(self): 
        response_json = json.loads(self.responseCreateUser.data)   
        assert self.responseCreateUser.status_code == 201
        assert 'id' in response_json
        assert 'createdAt' in response_json      

    # Función que valida la generacion exitosa del token
    def validate_success_generate_token(self):
        response_json = json.loads(self.responseToken.data)
        assert self.responseToken.status_code == 200
        assert 'id' in response_json
        assert 'expireAt' in response_json
        assert 'token' in response_json
        assert response_json['id'] == self.userId
        self.token = response_json['token']

    # Función que valida la actualización exitosa de un usuario
    def validate_success_update_user(self): 
        response_json = json.loads(self.responseUpdateUser.data)
        assert self.responseUpdateUser.status_code == 200
        assert 'msg' in response_json
        assert response_json['msg'] == 'el usuario ha sido actualizado'    

    # Función que valida la consulta exitosa de un usuario
    def validate_success_detail_user(self):
        response_json = json.loads(self.responseDetailUser.data)
        assert self.responseDetailUser.status_code == 200
        assert response_json["id"] == self.userId
        assert response_json["username"] == self.username
        assert response_json["email"] == self.email
        assert response_json["fullName"] == self.fullName
        assert response_json["dni"] == self.dni
        assert response_json["phoneNumber"] == self.phoneNumber
        assert response_json["status"] == "NO_VERIFICADO"        
        
    # Función que valida el request de la actualización de usuario
    def validate_bad_request_update_user(self): 
        response_json = json.loads(self.responseUpdateUser.data)
        assert self.responseUpdateUser.status_code == 400
        assert 'msg' in response_json
        assert response_json['msg'] == 'Párametros de entrada invalidos'         
         
    # Función que valida la creación exitosa de un usuario
    def test_create_new_user(self):
        # Creación nuevo usuario
        self.create_user_success()
        
    # Función que valida la creación de un usuario ya registrado    
    def test_existing_user_creation(self):
        # Creación nuevo usuario
        self.set_up()
        self.execute_create_user(self.data)
        self.validate_success_create_user()
        # Creación usuario existente
        self.execute_create_user(self.data)
        response_json = json.loads(self.responseCreateUser.data)
        assert self.responseCreateUser.status_code == 412
        assert 'msg' in response_json
        assert response_json['msg'] == 'El username ya se encuentra registrado' 

    # Función que valida la creación de un usuario cuando se envia un request invalido   
    def test_create_user_bad_request(self):
        # Creación nuevo usuario
        self.set_up()
        data = { "fullName": f"{self.fullName}" }
        self.execute_create_user(data)
        response_json = json.loads(self.responseCreateUser.data)
        assert self.responseCreateUser.status_code == 400
        assert 'msg' in response_json
        assert response_json['msg'] == 'Párametros de entrada invalidos'         
           
    # Función que valida la actualización exitosa de un usuario
    def test_update_user(self):
        # Creación nuevo usuario
        self.create_user_success()
        # Actualización de usuario
        self.set_up()
        self.update_user(self.userId, None)
        self.validate_success_update_user()
        
    # Función que valida el request vacio
    def test_update_user_empty_request(self):
        # Creación nuevo usuario
        self.create_user_success()
        # Actualización de usuario
        self.update_user(self.userId, {})
        response_json = json.loads(self.responseUpdateUser.data)
        self.validate_bad_request_update_user()
        
    # Función que valida los parametros de entrada
    def test_update_user_bad_request(self):
        # Creación nuevo usuario
        self.create_user_success()
        # Actualización de usuario
        self.set_up()
        dataUpdate = {
                "email": f"{self.email}"
            }
        # Actualización de usuario
        self.update_user(self.userId, dataUpdate)
        response_json = json.loads(self.responseUpdateUser.data)
        self.validate_bad_request_update_user()         

    # Función que valida la actualizacion de un usuario no registrado
    def test_update_user_non_existent(self):
        # Actualización de usuario
        userId = uuid.uuid4()
        self.set_up()
        self.update_user(userId, None)
        response_json = json.loads(self.responseUpdateUser.data)
        assert self.responseUpdateUser.status_code == 404
        assert 'msg' in response_json
        assert response_json['msg'] == 'El usuario no se encuentra registrado'          
        
    # Función que valida la generación exitosa del token
    def test_generate_token(self):
        #Creación usuario y generación token
        self.create_user_generate_token_success()

    # Función que valida la generación del token con credenciales erroneas
    def test_generate_token_wrong_credentials(self):
        # Creación nuevo usuario
        self.create_user_success()
        # Generación token
        dataAuthenticate = {
            "username": f"{self.username}",
            "password": f"{self.password}wrong"
        }
        self.execute_generate_token(dataAuthenticate)
        response_json = json.loads(self.responseToken.data)
        assert self.responseToken.status_code == 404
        assert 'msg' in response_json
        assert response_json['msg'] == 'El password es incorrecto'   

    # Función que valida la generación del token con un request invalido
    def test_generate_token_bad_request(self):
        # Creación nuevo usuario
        self.create_user_success()
        # Generación token
        dataAuthenticate = {
            "username": f"{self.username}"
        }
        self.execute_generate_token(dataAuthenticate)
        response_json = json.loads(self.responseToken.data)
        assert self.responseToken.status_code == 400
        assert 'msg' in response_json
        assert response_json['msg'] == 'Párametros de entrada invalidos'          
        
    # Función que valida la generación del token con un usuario no existente
    def test_generate_token_user_non_existent(self):        
        # Generación token
        dataAuthenticate = {
                "username": "fake",
                "password": "fake"
            }
        self.execute_generate_token(dataAuthenticate)
        response_json = json.loads(self.responseToken.data)
        assert self.responseToken.status_code == 404
        assert 'msg' in response_json
        assert response_json['msg'] == 'El usuario no se encuentra registrado'
        
    # Función que limpia todos los usuarios registrados
    def test_reset_users(self):
        # Reset tabla usuarios
        data = {}
        with app.test_client() as test_client:
            response = test_client.post(
                '/users/reset', json=data
            )
            response_json = json.loads(response.data)
        assert response.status_code == 200
        assert 'msg' in response_json
        assert response_json['msg'] == 'Todos los datos fueron eliminados'
        
    # Función que valida el estado del servidor
    def test_health_check(self):
        # Reset tabla usuarios
        with app.test_client() as test_client:
            response = test_client.get(
                '/users/ping'
            )
            data = str(response.data)
        assert response.status_code == 200
        assert 'pong' in data
        
    # Función que consulta exitosamente el detalle del usuario
    def test_detail_user(self):
        # Creación usuario y generación token
        self.create_user_generate_token_success()
        # Consulta de usuario
        headers = {}
        headers["Authorization"] = f"Bearer {self.token}"
        self.execute_detail_user(headers)
        self.validate_success_detail_user()

    # Función que valida la consulta del usuario sin enviar el token
    def test_detail_user_without_token(self):
        # Creación usuario y generación token
        self.create_user_generate_token_success()
        # Consulta de usuario
        headers = {}
        self.execute_detail_user(headers)
        response_json = json.loads(self.responseDetailUser.data)
        assert self.responseDetailUser.status_code == 403
        assert 'msg' in response_json
        assert response_json['msg'] == 'El token no está en el encabezado de la solicitud'
        
    # Función que valida la consulta del usuario enviando un token invalido
    def test_detail_user_invalid_token(self):
        # Creación usuario y generación token
        self.create_user_generate_token_success()
        # Consulta de usuario
        headers = {}
        headers["Authorization"] = f"Bearer {self.token}fake"
        self.execute_detail_user(headers)
        response_json = json.loads(self.responseDetailUser.data)
        assert self.responseDetailUser.status_code == 401
        assert 'msg' in response_json
        assert response_json['msg'] == 'El token no es válido o está vencido'
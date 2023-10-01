from src.commands.create import CreateOffer
from faker import Faker
from httmock import HTTMock
from uuid import uuid1
import src.main
import tests.mocks
import random

class TestCreate():   
    
    def set_up(self):
        self.dataFactory = Faker()
        self.userId = self.dataFactory.uuid4()
        self.postId = "db29e615-4f25-11ee-99f7-c89402273298"
        self.description = self.dataFactory.sentence(nb_words=4)
        self.size = random.choice(["LARGE", "MEDIUM", "SMALL"])
        self.fragile = random.choice([True, False])
        self.offer = float(self.dataFactory.pydecimal(left_digits=6, right_digits=2, positive=True))
        self.data = {
                      "postId": self.postId,
                      "description":self.description,
                      "size": self.size,
                      "fragile": self.fragile,
                      "offer": self.offer
                    }
    
    def set_up_bad_request(self):
        self.dataFactory = Faker()
        self.userId = self.dataFactory.uuid4()
        self.postId = self.dataFactory.uuid4()
        self.description = self.dataFactory.sentence(nb_words=4)
        self.size = random.choice(["LARGE", "MEDIUM", "SMALL"])
        self.fragile = random.choice([True, False])
        self.offer = self.dataFactory.pydecimal(left_digits=6, right_digits=2, positive=True)
        self.data = {
                      "postId": self.postId,
                      "description":self.description,
                      "size": self.size,
                      "fragile" : self.fragile                    
                    }    

    def test_failed_auth(self):
        self.set_up()
        with src.main.app.test_client() as test_client:           
            with HTTMock(tests.mocks.mock_failed_auth):
                response = test_client.post(f"/rf004/posts/{self.postId}/offers", json=self.data, headers={"Authorization": f"Bearer {uuid1()}"}) 
        assert response.status_code == 401


    def test_forbidden_auth(self):
        self.set_up()
        with src.main.app.test_client() as test_client:
            with HTTMock(tests.mocks.mock_forbidden_auth):
                response = test_client.post(f"/rf004/posts/{self.postId}/offers", json=self.data, headers={"Authorization": f"Bearer {uuid1()}"})
        assert response.status_code == 403


    def test_schema(self):
        self.set_up_bad_request()
        with src.main.app.test_client() as test_client:
            with HTTMock(tests.mocks.mock_success_auth):
                response = test_client.post(f"/rf004/posts/{self.postId}/offers", json=self.data, headers={"Authorization": f"Bearer {uuid1()}"})
        assert response.status_code == 400
    

    def test_post_expiration(self):
        self.set_up()
        postId = "db29e615-4f25-11ee-99f7-c89402273298"
        with src.main.app.test_client() as test_client:
            with HTTMock(tests.mocks.mock_success_auth, tests.mocks.mock_post_expired):                
                response = test_client.post(f"/rf004/posts/{postId}/offers", json=self.data, headers={"Authorization": f"Bearer {uuid1()}"})
        assert response.status_code == 412
    

    def test_post_invalid_owner(self):
        self.set_up()
        postId = "41f37778-5201-11ee-839c-c89402273298"        
        with src.main.app.test_client() as test_client:
            with HTTMock(tests.mocks.mock_success_auth, tests.mocks.mock_post_expired, tests.mocks.mock_post_invalid_owner):                
                response = test_client.post(f"/rf004/posts/{postId}/offers", json=self.data, headers={"Authorization": f"Bearer {uuid1()}"})
        assert response.status_code == 412
   

    def test_post_invalid_id(self):
        self.set_up()
        postId = "12345"
        with src.main.app.test_client() as test_client:
            with HTTMock(tests.mocks.mock_success_auth, tests.mocks.mock_post_expired, tests.mocks.mock_post_invalid_owner, tests.mocks.mock_post_invalid_id):                
                response = test_client.post(f"/rf004/posts/{postId}/offers", json=self.data, headers={"Authorization": f"Bearer {uuid1()}"})
        assert response.status_code == 404


    def test_post_id_doesnt_exist(self):
        self.set_up()
        postId = "8c749f81-5205-11ee-b059-c89402273298"
        with src.main.app.test_client() as test_client:
            with HTTMock(tests.mocks.mock_success_auth, tests.mocks.mock_post_expired, tests.mocks.mock_post_invalid_owner, tests.mocks.mock_post_id_doesnt_exist):                
                response = test_client.post(f"/rf004/posts/{postId}/offers", json=self.data, headers={"Authorization": f"Bearer {uuid1()}"})
        assert response.status_code == 404
    
    
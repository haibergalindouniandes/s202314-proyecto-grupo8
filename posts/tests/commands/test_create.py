from src.commands.create import CreatePost
from faker import Faker
from datetime import datetime, timedelta
import src.main

class TestCreate():

    dataFactory = Faker()
    userId = None
    routeId = None
    expireAt = None    
    data = {}
    
    def set_up(self):
        self.userId = self.dataFactory.uuid4()
        self.routeId = self.dataFactory.uuid4()
        self.expireAt = (datetime.now() + timedelta(days=self.dataFactory.random_int(1, 30))).replace(microsecond=0).isoformat()
        self.data = {
            "routeId": f"{self.routeId}",
            "expireAt": f"{self.expireAt}"
        }
    
    def test_create_post(self):
        self.set_up()
        result = CreatePost(self.data, self.userId).execute()
        assert result != None

    def test_create_post_param_missing(self):
        try:           
            self.set_up()
            data2 = {
            "routeId": f"{self.routeId}"           
            }
            CreatePost(data2, self.userId).execute()
            assert 0 == 1
        except Exception as e:
            assert e.code == 400

    def test_create_post_wrong_expireDate(self):
        try:            
            self.set_up()
            data3 = {
                      "routeId": f"{self.routeId}",
                      "expireAt": (datetime.now() - timedelta(days=self.dataFactory.random_int(1, 30))).replace(microsecond=0).isoformat()
                    }
            CreatePost(data3, self.userId).execute()
            assert 0 == 1
        except Exception as e:
            assert e.code == 412

    def test_create_post_wrong_routeId(self):
        try:            
            self.set_up()
            data4 = {
                      "routeId": "xxxxxxxx-422b-11ee-a15b-c89402273298",
                      "expireAt": (datetime.now() + timedelta(days=self.dataFactory.random_int(1, 30))).replace(microsecond=0).isoformat()
                     }
            CreatePost(data4, self.userId).execute()
            assert 0 == 1
        except Exception as e:
            assert e.code == 400
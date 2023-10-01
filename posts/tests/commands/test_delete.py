from src.commands.create import CreatePost
from src.commands.delete import DeletePost
from src.commands.get import GetPost
from faker import Faker
from datetime import datetime, timedelta
import uuid


class TestDelete():

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

    def create_post(self):
        result = CreatePost(self.data, self.userId).execute()
        assert result != None
        self.postId = result.id

    def test_delete_post(self):
        try:
            self.set_up()
            self.create_post()
            DeletePost(self.postId).execute()
            GetPost(self.postId).execute()
            assert 0 == 1
        except Exception as e:
            assert e.code == 404

    def test_delete_post_id_inexisting(self):
        try:
            postId = str(uuid.uuid4())
            DeletePost(postId).execute()
            assert 0 == 1
        except Exception as e:
            assert e.code == 404
    
    def test_delete_post_id_wrong_format(self):
        try:
            postId = "xxxxxxxx-422b-11ee-a15b-c89402273298"
            DeletePost(postId).execute()
            assert 0 == 1
        except Exception as e:
            assert e.code == 400



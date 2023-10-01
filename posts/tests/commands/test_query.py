from src.commands.create import CreatePost
from src.commands.query import QueryPost
from faker import Faker
from datetime import datetime, timedelta


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

    def test_query_post_no_params(self):
        self.set_up()
        self.create_post()
        result = QueryPost({'expire':None, 'route':None, 'owner':None}, self.userId).execute()
        assert result != None

    def test_query_post_only_expire(self):
        self.set_up()
        self.create_post()
        result = QueryPost({'expire':'false', 'route':None, 'owner':None}, self.userId).execute()
        assert result != None

    def test_query_post_only_route(self):        
        self.set_up()
        self.create_post()
        result = QueryPost({'expire':None, 'route':self.routeId, 'owner':None}, self.userId).execute()
        assert result != None

    def test_query_post_only_owner(self):        
        self.set_up()
        self.create_post()
        result = QueryPost({'expire':None, 'route':None, 'owner':self.userId}, self.userId).execute()
        assert result != None        

    def test_query_post_expire_and_route(self):        
        self.set_up()
        self.create_post()
        result = QueryPost({'expire':'false', 'route':self.routeId, 'owner':None}, self.userId).execute()
        assert result != None

    def test_query_post_expire_and_owner(self):        
        self.set_up()
        self.create_post()
        result = QueryPost({'expire':'false', 'route':None, 'owner':self.userId}, self.userId).execute()
        assert result != None        

    def test_query_post_route_and_owner(self):        
        self.set_up()
        self.create_post()
        result = QueryPost({'expire':None, 'route':self.routeId, 'owner':self.userId}, self.userId).execute()
        assert result != None

    def test_query_post_wrong_expire(self):
        try:
            self.set_up()
            self.create_post()
            QueryPost({'expire':'falso', 'route':None, 'owner':None}, self.userId).execute()
            assert 0 == 1
        except Exception as e:
            assert e.code == 400

    def test_query_post_wrong_route(self):
        try:
            self.set_up()
            self.create_post()
            QueryPost({'expire':None, 'route':'xxxxxxxx-422b-11ee-a15b-c89402273298', 'owner':None}, self.userId).execute()
            assert 0 == 1
        except Exception as e:
            assert e.code == 400

    def test_query_post_wrong_owner(self):
        try:
            self.set_up()
            self.create_post()
            QueryPost({'expire':None, 'route':None, 'owner':'xxxxxxxx-422b-11ee-a15b-c89402273298'}, self.userId).execute()
            assert 0 == 1
        except Exception as e:
            assert e.code == 400

  
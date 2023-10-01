from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Creación de variable db
db = SQLAlchemy()

class Origin():
    airportCode : str
    country : str
    
    def __init__(self, airportCode, country):
        self.airportCode = airportCode
        self.country = country
    
    def obj_to_dict(self):  # for build json format
        return {
            "airportCode": self.country,
            "country": self.country
        }
    
class Destiny():
    airportCode : str
    country : str
    
    def __init__(self, airportCode, country):
        self.airportCode = airportCode
        self.country = country
        
    def obj_to_dict(self):  # for build json format
        return {
            "airportCode": self.country,
            "country": self.country
        }
    
    
class Route():
    id : str
    flightId : str
    origin : Origin
    destiny: Destiny
    bagCost: str
    
    def __init__(self,id, flightId, origin,destiny,bagCost):
        self.id = id
        self.flightId = flightId
        self.origin = origin
        self.destiny = destiny
        self.bagCost = bagCost
    
    def obj_to_dict(self):  # for build json format
        return {
            "id": self.id,
            "flightId": self.flightId,
            "origin": self.origin,
            "destiny": self.destiny,
            "bagCost": self.bagcost
        }
    
    
class Offers():
    id : str
    postId : str
    description : str
    size : str
    fragile : str
    offer : str
    score : float
    createdAt : datetime
    userId : str
    
    def __init__(self,id, postId, description,size,fragile,offer,score,createdAt, userId):
        self.id = id
        self.postId = postId
        self.description = description
        self.size = size
        self.fragile = fragile
        self.offer = offer
        self.score = score
        self.createdAt = createdAt
        self.userId = userId
    
    def obj_to_dict(self):  # for build json format
        return {
            "id": self.id,
            "postId" : self.postId,            
            "description": self.description,
            "size": self.size,
            "fragile": self.fragile,
            "offer": self.offer,
            "score": self.score,
            "createdAt": self.createdAt,
            "userId": self.userId
        }
    
    
class Post():
    id : str
    expireAt : datetime
    route : Route
    plannedStartDate : str
    plannedEndDate : str
    createdAt : datetime
    offers : Offers


    def __init__(self, id, expireAt, route, plannedStartDate, plannedEndDate, createdAt, offers ):
        self.id = id
        self.expireAt = expireAt
        self.route = route
        self.plannedStartDate =  plannedStartDate
        self.plannedEndDate = plannedEndDate
        self.createdAt = createdAt
        self.offers = offers

    def obj_to_dict(self):  # for build json format
        return {
            "id": self.id,
            "expireAt": self.expireAt,
            "route": self.route,
            "plannedStartDate": self.plannedStartDate,
            "plannedEndDate": self.plannedEndDate,
            "createdAt": self.createdAt,
            "score": self.score,
            "offers": self.offers,
        }
        

class Data():    
    data : Post
    
    def __init__(self, data):
        self.data = data
    

    def obj_to_dict(self):  # for build json format
        return {
            "data": self.data
        }
        
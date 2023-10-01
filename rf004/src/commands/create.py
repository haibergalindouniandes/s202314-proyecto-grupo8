from commands.base_command import BaseCommannd
from errors.errors import ApiError
from validators.validators import validateSchema, createOfferSchema, validatePostId, validatePostExpired, validatePostOwner 
import requests
import traceback
import os


class CreateOffer(BaseCommannd):
    def __init__(self, postId, post_request_json, headers):
        self.validateRequest(postId, post_request_json, headers)
    
    def validateRequest(self, postId, post_request_json, headers):        
        validateSchema(post_request_json, createOfferSchema)
        validatePostExpired(postId, headers)
        validatePostOwner(postId, headers)
        result_post = validatePostId(postId, headers)
        routeId = result_post.json()["routeId"]
        self.bagCost = self.getBagCost(routeId, headers)
        self.headers = headers
        self.postId = postId
        self.description = post_request_json["description"]
        self.size = post_request_json["size"]
        self.fragile = post_request_json["fragile"]
        self.offer = post_request_json["offer"]

    def getBagCost(self, routeId, headers):
        ROUTES_PATH = os.environ["ROUTES_PATH"]
        result_route = requests.get(f"{ROUTES_PATH}/routes/{routeId}", headers=headers)
        return result_route.json()["bagCost"]

    def execute(self):
        try:
            data_offer = {"postId": self.postId,
                          "description": self.description,
                          "size": self.size,
                          "fragile": self.fragile,
                          "offer": self.offer
                         }
            OFFERS_PATH = os.environ["OFFERS_PATH"]            
            result_offer = requests.post(f"{OFFERS_PATH}/offers", json=data_offer, headers=self.headers)
            data_score = {"packageAmount": str(self.bagCost),
                          "packageSize": self.size,
                          "offerAmount": str(self.offer),
                          "packageDescription": self.description,
                          "isPackageFragile": self.fragile,
                          "offerId": result_offer.json()["id"],
                          "postId": self.postId,
                          "userId": result_offer.json()["userId"]
                         }            
            SCORES_PATH = os.environ["SCORES_PATH"]
            result_score = requests.post(f"{SCORES_PATH}/scores", json=data_score, headers=self.headers)
            return result_offer, result_score
        except Exception as e:
            traceback.print_exc()
            raise ApiError(e)
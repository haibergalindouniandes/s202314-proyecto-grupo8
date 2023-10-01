from datetime import datetime

class Score():
    createdAt : str
    id : str
    isPackageFragile: str
    offerAmount : str
    offerId : str
    packageAmount : str
    packageDescription : str
    packageSize : str
    postId : str
    score: str
    userId : str
    
    def __init__(self,createdAt, id, isPackageFragile,offerAmount ,offerId,packageAmount,
                 packageDescription,packageSize,postId,score,userId):        
        self.createdAt = createdAt
        self.id = id
        self.isPackageFragile =isPackageFragile
        self.offerAmount =offerAmount
        self.offerId =offerId
        self.packageAmount = packageAmount
        self.packageDescription = packageDescription
        self.packageSize = packageSize
        self.postId = postId
        self.score = score
        self.userId = userId
        
    
    def obj_to_dict(self):  # for build json format
        return {
            "createdAt":self.createdAt,
            "id":self.id,
            "isPackageFragile":self.isPackageFragile,
            "offerAmount":self.offerAmount,
            "offerId":self.offerId,
            "packageAmount":self.packageAmount,
            "packageDescription":self.packageDescription,
            "packageSize":self.packageSize,
            "postId":self.postId,
            "score":self.score,
            "userId":self.userId,
        }


    
class Offer():
    id : str
    postId : str
    description : str    
    size: str
    fragile: str
    offer: str
    createdAt: str
    userId : str
   
    
    
    def __init__(self,id,postId,description, size, fragile, offer, createdAt, userId):                
        self.id = id
        self.postId = postId
        self.description = description
        self.size = size
        self.fragile = fragile
        self.offer = offer
        self.createdAt = createdAt
        self.userId = userId
        
        
    
    def obj_to_dict(self):  # for build json format
        return {
            "id": self.id,
            "postId": self.postId,
            "description": self.description,
            "size": self.size,
            "fragile": self.fragile,
            "offer": self.offer,
            "createdAt": self.createdAt,
            "userId": self.userId,
        }
    
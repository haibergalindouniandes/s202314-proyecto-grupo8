# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError, NotFound
from models.models import db, Offer
from sqlalchemy.exc import SQLAlchemyError
from validators.validators import validateIDsUUID
import traceback

def dict_helper(objlist):
    result2 = [item.obj_to_dict() for item in objlist]
    return result2

# Clase que contiene la logica de creción de usuarios
class ListOffer(BaseCommannd):
    def __init__(self, post, owner):
        self.post = post
        self.owner = owner

    # Función que realiza creación del usuario
    def execute(self):
        try:
            if(self.post == None and self.owner == None):
                offerList = Offer.query.all()
            elif(self.post == None and self.owner != None):
                validateIDsUUID(self.owner)
                offerList = Offer.query.filter(Offer.userId == self.owner)
            elif(self.owner == None and self.post != None):
                validateIDsUUID(self.post)
                offerList = Offer.query.filter(Offer.postId == self.post)
            else:
                validateIDsUUID(self.owner)
                validateIDsUUID(self.post)
                offerList = Offer.query.filter(Offer.userId == self.owner).filter(Offer.postId == self.post)
            return dict_helper(offerList)
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)
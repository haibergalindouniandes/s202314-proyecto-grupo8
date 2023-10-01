from commands.base_command import BaseCommannd
from errors.errors import ApiError
from validators.validators import validateSchema, validateUUID, validateDateString, createPostSchema
from models.model import db, Post
from sqlalchemy.exc import SQLAlchemyError
import uuid
import traceback
from datetime import datetime
from dateutil.parser import parse


class CreatePost(BaseCommannd):
    def __init__(self, post_request_json, userId):
        self.validateRequest(post_request_json, userId)
    
    def validateRequest(self, post_request_json, userId):
        validateSchema(post_request_json, createPostSchema)
        validateUUID(post_request_json['routeId'])        
        validateDateString(post_request_json['expireAt'])            
        self.id = str(uuid.uuid1())
        self.routeId = post_request_json['routeId']
        self.userId = userId
        self.createdAt = datetime.now()
        self.expireAt = parse(post_request_json['expireAt'])

    def execute(self):
        try:    
            new_post = Post(id=self.id, 
                            routeId=self.routeId, 
                            userId=self.userId,
                            createdAt=self.createdAt,
                            expireAt=self.expireAt)
            db.session.add(new_post)
            db.session.commit()
            return new_post
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)
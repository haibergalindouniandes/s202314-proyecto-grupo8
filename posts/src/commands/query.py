from commands.base_command import BaseCommannd
from errors.errors import ApiError, BadRequest
from validators.validators import validateUUID
from models.model import Post
from sqlalchemy.exc import SQLAlchemyError
import traceback
from datetime import datetime


class QueryPost(BaseCommannd):
    def __init__(self, post_request_args, userId):
        self.checkArguments(post_request_args, userId)
    
    def checkArguments(self, post_request_args, userId):
        self.expire = post_request_args.get('expire')
        self.route = post_request_args.get('route')
        self.owner = post_request_args.get('owner')
        if self.expire:
            if self.expire.lower() != 'true' and self.expire.lower() != 'false':
                raise BadRequest
        if self.route:
            validateUUID(self.route)
        if self.owner=='me':
            self.owner = userId
        elif self.owner is not None:
            validateUUID(self.owner)
   
    def execute(self):
        try:
            if self.expire or self.route or self.owner:
                if self.expire:
                    if self.expire.lower() == 'true':
                        if self.route and self.owner:
                            return Post.query.filter(Post.expireAt<datetime.now(), Post.routeId==self.route, Post.userId==self.owner)
                        elif self.route and not self.owner:
                            return Post.query.filter(Post.expireAt<datetime.now(), Post.routeId==self.route)
                        elif self.owner and not self.route:
                            return Post.query.filter(Post.expireAt<datetime.now(), Post.userId==self.owner)
                        else:
                            return Post.query.filter(Post.expireAt<datetime.now())
                    elif self.expire.lower() == 'false':
                        if self.route and self.owner:
                            return Post.query.filter(Post.expireAt>=datetime.now(), Post.routeId==self.route, Post.userId==self.owner)
                        elif self.route and not self.owner:
                            return Post.query.filter(Post.expireAt>=datetime.now(), Post.routeId==self.route)
                        elif self.owner and not self.route:
                            return Post.query.filter(Post.expireAt>=datetime.now(), Post.userId==self.owner)
                        else:
                            return Post.query.filter(Post.expireAt>=datetime.now())
                else:    
                    if self.route and self.owner:
                        return Post.query.filter(Post.routeId==self.route, Post.userId==self.owner)
                    elif self.route and not self.owner:
                        return Post.query.filter(Post.routeId==self.route)
                    elif self.owner and not self.route:
                        return Post.query.filter(Post.userId==self.owner)
            else:
                return Post.query.all()
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)       

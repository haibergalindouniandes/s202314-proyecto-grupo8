from commands.base_command import BaseCommannd
from errors.errors import ApiError, PostDoNotExist
from validators.validators import validateUUID
from models.model import db, Post
from sqlalchemy.exc import SQLAlchemyError
import traceback


class DeletePost(BaseCommannd):
    def __init__(self, postId):
        self.validateRequest(postId)

    def validateRequest(self, postId):
        self.postId = postId
        validateUUID(self.postId)

    def execute(self):
        try:
            post = Post.query.filter(Post.id == self.postId).first()
            if post is None:
                raise PostDoNotExist
            Post.query.filter(Post.id == self.postId).delete()   
            db.session.commit()
        except SQLAlchemyError as e:
            traceback.print_exc()
            raise ApiError(e)
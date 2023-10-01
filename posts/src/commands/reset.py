from commands.base_command import BaseCommannd
from errors.errors import ApiError
from models.model import db, Post
import traceback


class ResetPosts(BaseCommannd):
    
    def execute(self):
        try:
            db.session.query(Post).delete()
            db.session.commit()
        except Exception as e:
            traceback.print_exc()
            raise ApiError(e)
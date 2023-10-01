from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Post(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    routeId = db.Column(db.String(64))
    userId = db.Column(db.String(64))
    createdAt = db.Column(db.DateTime)
    expireAt = db.Column(db.DateTime)

class PostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True

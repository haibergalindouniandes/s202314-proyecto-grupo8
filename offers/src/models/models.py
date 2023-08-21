# Importación de dependencias
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from sqlalchemy import DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid

# Creación de variable db
db = SQLAlchemy()

# Clase que cotiene la definición del modelo de base de datos de Usuario
class Offer(db.Model):
    __tablename__ = "offers"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    postId = db.Column(db.String(64), unique=True, nullable=False)
    userId = db.Column(db.String(64), nullable=True)
    description = db.Column(db.String(140), nullable=False)
    size = db.Column(db.String(140), default="SMALL", nullable=False)
    fragile = db.Column(db.Boolean,default=True, nullable=False)
    offer = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    createdAt = db.Column(DateTime, default=datetime.utcnow)

    def obj_to_dict(self):  # for build json format
        return {
            "id": self.id,
            "postId": self.postId,
            "userId": self.userId,
            "description": self.description,
            "size": self.size,
            "fragile": self.fragile,
            "offer": self.offer,
            "createdAt": self.createdAt
        }

# Clase que autogenera el esquema del modelo Usuario
class OfferSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Offer
        id = fields.String() 
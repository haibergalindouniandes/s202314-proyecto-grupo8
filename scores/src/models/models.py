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
class Score(db.Model):
    __tablename__ = "scores"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    packageDescription = db.Column(db.String(200))
    packageSize = db.Column(db.String(6))
    packageAmount = db.Column(db.Numeric(10,2))
    isPackageFragile = db.Column(db.Boolean)
    offerAmount = db.Column(db.Numeric(10,2))
    score = db.Column(db.Numeric(10,2))
    offerId = db.Column(UUID(as_uuid=True))
    postId = db.Column(UUID(as_uuid=True))
    userId = db.Column(UUID(as_uuid=True))
    createdAt = db.Column(DateTime, default=datetime.utcnow)

# Clase que autogenera el esquema del modelo Usuario
class ScoreSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Score
        id = fields.String() 
        
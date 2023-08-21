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
class User(db.Model):
    __tablename__ = "users"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    phoneNumber = db.Column(db.String(20), nullable=True)
    dni = db.Column(db.String(20), nullable=True)
    fullName = db.Column(db.String(200), nullable=True)
    password = db.Column(db.String(128))
    salt = db.Column(db.String(64))
    token = db.Column(db.String(36), nullable=True)
    status = db.Column(db.String(13), default="NO_VERIFICADO")
    expireAt = db.Column(DateTime, nullable=True)
    createdAt = db.Column(DateTime, default=datetime.utcnow)
    updatedAt = db.Column(DateTime, default=datetime.utcnow)

# Clase que autogenera el esquema del modelo Usuario
class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        id = fields.String() 
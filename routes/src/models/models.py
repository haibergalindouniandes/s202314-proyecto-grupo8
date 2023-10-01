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

# Clase que cotiene la definición del modelo de base de datos de trayectos
class Route(db.Model):
    __tablename__ = "routes"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    flightId = db.Column(db.String(5), unique=True)
    sourceAirportCode = db.Column(db.String(5),nullable=True)
    sourceCountry = db.Column(db.String(64), nullable=True)
    destinyAirportCode = db.Column(db.String(5), nullable=True)
    destinyCountry = db.Column(db.String(64), nullable=True)
    bagCost = db.Column(db.Integer())
    plannedStartDate = db.Column(DateTime, nullable=True)
    plannedEndDate = db.Column(DateTime, nullable=True)    
    createdAt = db.Column(DateTime, default=datetime.utcnow)
    updatedAt = db.Column(DateTime, default=datetime.utcnow)

    def obj_to_dict(self):  # for build json format
        return {
            "id": self.id,
            "flightId": self.flightId,
            "sourceAirportCode": self.sourceAirportCode,
            "sourceCountry": self.sourceCountry,
            "destinyAirportCode": self.destinyAirportCode,
            "destinyCountry": self.destinyCountry,
            "bagCost": self.bagCost,
            "plannedStartDate": self.plannedStartDate,
            "plannedEndDate": self.plannedEndDate,
            "createdAt": self.createdAt
        }


# Clase que autogenera el esquema del modelo Usuario
class RouteSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Route
        id = fields.String() 
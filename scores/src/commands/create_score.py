# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError
from validators.validators import validateSchema, createScoreSchema
from models.models import db, Score, ScoreSchema
from sqlalchemy.exc import SQLAlchemyError
import traceback

# Instanciación del esqumemas
scoreSchema = ScoreSchema()

# Clase que contiene la logica de creción de utilidad
class CreateScore(BaseCommannd):
    def __init__(self, request):
        validateSchema(request, createScoreSchema)
        self.scoreRequest = request

    # Función que permite obtener el porcentaje de ocupación
    def calculatePercentageOccupancy(self, packageSize):# pragma: no cover 
        if packageSize == 'MEDIUM':
            return 0.5
        if packageSize == 'SMALL':
            return 0.25
        return 1

    # Función que permite generar el password
    def calculateScore(self, packageAmount, packageSize, offerAmount):
        return offerAmount - (self.calculatePercentageOccupancy(packageSize) * packageAmount)	

    # Función que realiza creación de la utilidad
    def execute(self):
        try:
            # Calculo de la utilidad
            score = self.calculateScore(float(self.scoreRequest['packageAmount']),
                                        self.scoreRequest['packageSize'], 
                                        float(self.scoreRequest['offerAmount']))
            # Inserción de la utilidad en base de datos
            newScore = Score(packageDescription=self.scoreRequest['packageDescription'],
                            packageSize=self.scoreRequest['packageSize'],
                            packageAmount=float(self.scoreRequest['packageAmount']),
                            isPackageFragile=self.scoreRequest['isPackageFragile'],
                            offerAmount=float(self.scoreRequest['offerAmount']),
                            score=score,
                            offerId=self.scoreRequest['offerId'],
                            postId=self.scoreRequest['postId'],
                            userId=self.scoreRequest['userId'])
            db.session.add(newScore)
            db.session.commit()
            return scoreSchema.dump(newScore)
        except SQLAlchemyError as e:  # pragma: no cover
            traceback.print_exc()
            raise ApiError(e)
        

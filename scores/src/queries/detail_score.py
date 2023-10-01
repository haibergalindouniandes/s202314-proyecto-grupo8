# Importación de dependencias
from queries.base_query import BaseQuery
from errors.errors import ApiError, ScoresNotFound
from models.models import Score, ScoreSchema
from sqlalchemy.exc import SQLAlchemyError
from validators.validators import validateUuid
import traceback

# Instanciación del esqumemas
scoreSchema = ScoreSchema()

# Clase que contiene la logica de consulta de utilidades
class DetailScore(BaseQuery):
    def __init__(self, id):
        validateUuid(id)
        self.id = id
    
    # Función que realiza la consulta de las utilidades
    def query(self):
        try:
            score = Score.query.filter(Score.id == self.id).first()
            if score == None:
                raise ScoresNotFound
            return scoreSchema.dump(score)
        except SQLAlchemyError as e:# pragma: no cover
            traceback.print_exc()
            raise ApiError(e)


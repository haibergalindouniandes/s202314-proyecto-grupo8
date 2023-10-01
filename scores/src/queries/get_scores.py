# Importación de dependencias
from queries.base_query import BaseQuery
from errors.errors import ApiError, ScoresNotFound
from models.models import Score, ScoreSchema
from sqlalchemy.exc import SQLAlchemyError
import traceback

# Instanciación de esqumemas
scoreSchema = ScoreSchema()

# Clase que contiene la logica de consulta de utilidades
class GetScores(BaseQuery):

    # Función que realiza la consulta de las utilidades
    def query(self):
        try:
            scores = Score.query.all()
            if len(scores) == 0:
                raise ScoresNotFound
            return [scoreSchema.dump(score) for score in scores]
        except SQLAlchemyError as e:# pragma: no cover
            traceback.print_exc()
            raise ApiError(e)

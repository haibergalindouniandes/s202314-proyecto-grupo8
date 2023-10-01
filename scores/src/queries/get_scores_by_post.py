# Importación de dependencias
from queries.base_query import BaseQuery
from errors.errors import ApiError, ScoresNotFound
from models.models import Score, ScoreSchema
from sqlalchemy.exc import SQLAlchemyError
from validators.validators import validateUuid
import traceback

# Instanciación de esqumemas
scoreSchema = ScoreSchema()

# Clase que contiene la logica de creción de usuarios
class GetScoresByPost(BaseQuery):
    def __init__(self, postId):
        validateUuid(postId)
        self.postId = postId

    # Función que realiza la consulta de utilidades por Publicación
    def query(self):
        try:
            scores = Score.query.filter(Score.postId == self.postId).order_by(Score.score.desc()).all()
            if len(scores) == 0:
                raise ScoresNotFound
            return [scoreSchema.dump(score) for score in scores]
        except SQLAlchemyError as e:# pragma: no cover
            traceback.print_exc()
            raise ApiError(e)

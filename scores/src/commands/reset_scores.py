# Importación de dependencias
from commands.base_command import BaseCommannd
from errors.errors import ApiError
from models.models import db, Score
import traceback

# Clase que contiene la logica limpiar la tabla scores
class ResetScores(BaseCommannd):
    # Función que realiza creación del usuario
    def execute(self):
        try:
            db.session.query(Score).delete()
            db.session.commit()
            return True
        except Exception as e:# pragma: no cover
            traceback.print_exc()
            raise ApiError(e)
        

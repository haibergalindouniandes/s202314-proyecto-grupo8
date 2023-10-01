
# Clase que contiene la logica de las pruebas del servicio
from src.commands.reset_scores import ResetScores
import src.main

# Clase que contiene la logica de las pruebas del servicio
class TestResetScores():
    
    # Función que valida la limpieza exitosa de la tabla scores
    def test_create_new_score(self):
        # Limpieza de la tabla scores
        assert ResetScores().execute()
    
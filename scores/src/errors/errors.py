# Clase que contiene la estructura de error por defecto
class ApiError(Exception):
    code = 500
    description = "Error interno, por favor revise el log"
    
# Clase que contiene la estructura de error de tipo Not Found
class ScoresNotFound(ApiError):
    code = 404
    description = "No se encontraron datos"
    
# Clase que contiene la estructura de un error de tipo Bad Request
class BadRequest(ApiError):
    code = 400
    description = "Párametros de entrada invalidos"
    
# Clase que contiene la estructura de un error de un UUID invalido
class BadUuid(ApiError):
    code = 400
    description = "El ID ingresado es invalido"    
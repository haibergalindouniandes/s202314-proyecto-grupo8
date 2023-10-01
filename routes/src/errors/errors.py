# Clase que contiene la estructura de error por defecto
class ApiError(Exception):
    code = 500
    description = "Error interno, por favor revise el log"
    
# Clase que contiene la estructura de error cuando ya esta registrado el email
class FligthExists(ApiError):
    code = 412
    description = "El flightId ya existe."

class ValidateDates(ApiError):
    code = 412
    description = "Las fechas del trayecto no son válidas"


# Clase que contiene la estructura de error cuando no esta registra el password
class PasswordNotExists(ApiError):
    code = 404
    description = "El password es incorrecto"    
    
# Clase que contiene la estructura de error cuando el token no es valido o esta vencido
class InvalidToken(ApiError):
    code = 401
    description = "El token no es válido o está vencido" 
    
# Clase que contiene la estructura de error cuando no se envia el token
class MissingToken(ApiError):
    code = 403
    description = "No hay token en la solicitud"

# Clase que contiene la estructura de un error de tipo Bad Request
class BadRequest(ApiError):
    code = 400
    description = "Párametros de entrada invalidos"

# Clase que contiene la estructura de error cuando no se encuentra el ID
class NotFound(ApiError):
    code = 404
    description = "El trayecto con ese id no existe."

# Clase que contiene la estructura de error cuando el ID no esta en Formato UUID
class IdNotUUID(ApiError):
    code = 400
    description = "El ID dado no esta en formato UUID"

class validateFlightError(ApiError):
    code = 400    
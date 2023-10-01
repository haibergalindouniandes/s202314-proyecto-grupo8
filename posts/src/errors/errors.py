# Clase que contiene la estructura de error por defecto
class ApiError(Exception):
    code = 500
    description = "Error interno, por favor revise el log"
    
# Clase que contiene la estructura de un error de tipo Bad Request
class BadRequest(ApiError):
    code = 400
    description = "Alguno de los campos no esta presente en la solicitud, o no tiene el formato esperado."

# Clase que contiene la estructura de error cuando el ID no esta en Formato UUID
class InvalidUUID(ApiError):
    code = 400
    description = "El id no es un valor string con formato uuid"

# Clase que contiene la estructura de error cuando el token no es valido o esta vencido
class InvalidToken(ApiError):
    code = 401
    description = "El token no es válido o está vencido" 
    
# Clase que contiene la estructura de error cuando no se envia el token
class MissingToken(ApiError):
    code = 403
    description = "No hay token en la solicitud"

# Clase que contiene la estructura de error cuando el id de la publicacion solicitada no existe
class PostDoNotExist(ApiError):
    code = 404
    description = "La publicacion con ese id no existe"    

# Clase que contiene la estructura de error cuando la fecha de expiracion no es valida
class InvalidExpirationDate(ApiError):
    code = 412
    description = "La fecha expiración no es válida" 




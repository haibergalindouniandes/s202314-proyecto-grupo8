# Clase que contiene la estructura de error por defecto
class ApiError(Exception):
    code = 500
    description = "Error interno, por favor revise el log"
    
# Clase que contiene la estructura de error cuando el token no es valido o esta vencido
class InvalidToken(ApiError):
    code = 401
    description = "El token no es válido o está vencido"
    
# Clase que contiene la estructura de error cuando no se envia el token
class MissingToken(ApiError):
    code = 403
    description = "El token no está en el encabezado de la solicitud"

# Clase que contiene la estructura de un error de tipo Bad Request
class BadRequest(ApiError):
    code = 400
    description = "Párametros de entrada invalidos"
    
# Clase que contiene la estructura de un error de tipo Bad Request
class PostDoNotExist(ApiError):
    code = 404
    description = "La publicación a la que se quiere asociar la oferta no existe"    
    
# Clase que contiene la estructura de un error de tipo Bad Request
class PostExpired(ApiError):
    code = 412
    description = "La publicación ya está expirada y no se reciben más ofertas por ella"
    
# Clase que contiene la estructura de un error de tipo Bad Request
class PostInvalidOwner(ApiError):
    code = 412
    description = "La publicación es del mismo usuario y no se puede ofertar por ella" 
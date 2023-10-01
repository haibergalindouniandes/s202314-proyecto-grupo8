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
    description = "No hay token en la solicitud"
    
# Clase que contiene la estructura de error cuando no se encuentra el ID
class NotFound(ApiError):
    code = 404
    description = "La publicación no existe."
    
class InvalidUserPost(ApiError):
    code = 403
    description = "El usuario no tiene permiso para ver el contenido de esta publicación."
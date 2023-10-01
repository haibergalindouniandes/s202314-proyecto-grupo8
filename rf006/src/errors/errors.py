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

# Clase que contiene la estructura de un error cuando ya existe la tarje de credito
class CreditCardRepeated(ApiError):
    code = 409
    description = "Ya existe esa tarjeta de credito"

# Clase que contiene la estructura de error cuando la tarjeta de credito esta vencida
class CreditCardExpired(ApiError):
    code = 412
    description = "Tarjeta de credita expirada"

# Clase que contiene la estructura de error cuando TrueNative no genera token de la tarjeta
class MissingTrueNativeToken(ApiError):
    code = 400
    description = "TrueNative no genero token de la tarjeta"

# Clase que contiene la estructura de error por defecto
class ApiError(Exception):
    code = 500
    description = "Error interno, por favor revise el log"
    
# Clase que contiene la estructura de error cuando un campo esta mal para la creacion
class OfferFieldCreateError(ApiError):
    code = 412
    description = "Alguno de los Valores de la Nueva Oferta esta mal formulado"
    
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

# Clase que contiene la estructura de error cuando un campo esta mal para la busqueda
class OfferFieldSearchError(ApiError):
    code = 400
    description = "Alguno de los Valores para la busqueda de Ofertas esta mal formulado"

# Clase que contiene la estructura de error cuando el ID no esta en Formato UUID
class IdNotUUID(ApiError):
    code = 400
    description = "El ID dado no esta en formato UUID"

# Clase que contiene la estructura de error cuando no se encuentra el ID
class NotFound(ApiError):
    code = 404
    description = "La Oferta con ese id no existe."
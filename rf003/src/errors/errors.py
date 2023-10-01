# Clase que contiene la estructura de error por defecto
class ApiError(Exception):
    code = 500
    description = "Error interno, por favor revise el log"


class RouteDateError(ApiError):
    code = 412
    description = "Las fechas del trayecto no son válidas"


class ExpirationDateError(ApiError):
    code = 412
    description = "La fecha expiración no es válida"


class UserPostRouteError(ApiError):
    code = 412
    description = "El usuario ya tiene una publicación para la misma fecha"


class BadRequest(ApiError):
    code = 400
    description = "Párametros de entrada invalidos"

    # Clase que contiene la estructura de error cuando el token no es valido o esta vencido


class InvalidToken(ApiError):
    code = 401
    description = "El token no es válido o está vencido"


# Clase que contiene la estructura de error cuando no se envia el token
class MissingToken(ApiError):
    code = 403
    description = "No hay token en la solicitud"

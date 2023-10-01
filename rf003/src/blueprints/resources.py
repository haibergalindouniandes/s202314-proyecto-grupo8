from flask import Blueprint, request
from flask.json import jsonify
from validators.validators import (
    validateToken,
    validateDates,
    validateSchema,
    validate_expiration_date,
)
from agregators.post import post_user_route_check, rf003_post_create
from agregators.routes import route_check
from utilities.utilities import formatDateTimeToUTC
from errors.errors import RouteDateError, UserPostRouteError, ExpirationDateError
import traceback
from rollbacks.routes import RF003CreateRouteRollback


rf003_blueprint = Blueprint("rf003", __name__)


@rf003_blueprint.route("/rf003/ping", methods=["GET"])
def health():
    return "pong"


@rf003_blueprint.route("/rf003/posts", methods=["POST"])
def createPost():
    try:
        head = request.headers
        data = request.get_json()
        user = validateToken(head)
        validateSchema(data)
        route = route_check(data, head)
        if not validate_expiration_date(data["expireAt"]):
            RF003CreateRouteRollback().execute(head, route["id"])
            raise ExpirationDateError
        if not validateDates(data["plannedStartDate"], data["expireAt"]):
            RF003CreateRouteRollback().execute(head, route["id"])
            raise RouteDateError
        if not post_user_route_check(route["id"], user, head):
            RF003CreateRouteRollback().execute(head, route["id"])
            raise UserPostRouteError
        result = rf003_post_create(route["id"], data["expireAt"], head)
        return (
            jsonify(
                {
                    "data": {
                        "id": result["id"],
                        "userId": result["userId"],
                        "createdAt": formatDateTimeToUTC(str(result["createdAt"])),
                        "expireAt": data["expireAt"],
                        "route": {
                            "id": route["id"],
                            "createdAt": formatDateTimeToUTC(str(route["createdAt"])),
                        },
                    },
                    "msg": "Publicacion creada Exitosamente",
                }
            ),
            201,
        )
    except RouteDateError as e:
        traceback.print_exc()
        raise RouteDateError(e)
    except UserPostRouteError as e:
        traceback.print_exc()
        raise UserPostRouteError(e)

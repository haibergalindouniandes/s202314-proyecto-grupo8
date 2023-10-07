from jsonschema import ValidationError
from flask import request, jsonify, Blueprint
from flask_expects_json import expects_json

from controllers.users_controller import create_task
from db import DatabaseClient
from utils import validate_token
from errors import TransactionAlreadyRequested, NoHeaderToken, InvalidToken


SCHEMA = {
    "type": "object",
    "properties": {
        "transactionIdentifier": {"type": "string"},
        "userIdentifier": {"type": "string"},
        "userWebhook": {"type": "string"},
        "user": {
            "type": "object",
            "properties": {
                "email": {"type": "string"},
            }
        }
    },
    "required": ["transactionIdentifier", "userIdentifier", "userWebhook", "user"]
}

users_blueprint = Blueprint("users", __name__)


@users_blueprint.route("/native/verify", methods=["POST"])
@expects_json(SCHEMA)
def verify():
    try:
        if request.method == "POST":
            validate_token(request.headers)
            user_id = request.json["userIdentifier"]
            transaction_id = request.json["transactionIdentifier"]
            user = request.json["user"]
            webhook = request.json["userWebhook"]
            data = create_task(user_id, transaction_id, user, webhook)
            return jsonify(data), 201
    except TransactionAlreadyRequested as err:
        return jsonify({"error": str(err)}), 409
    except InvalidToken:
        return jsonify({"error": "Token is required"}), 403
    except NoHeaderToken:
        return jsonify({"error": "Invalid token"}), 401


@users_blueprint.route("/native/verify/log", methods = ["GET", "DELETE"])
def verify_log():
    db = DatabaseClient("users")
    if request.method == "GET":
        data = db.get_all()
        return jsonify(data), 200
    if request.method == "DELETE":
        db.clean()
        return dict(), 200


@users_blueprint.route("/native/verify/log/<ruv>", methods = ["GET"])
def verify_log_detail(ruv):
    if request.method == "GET":
        db = DatabaseClient("users")
        data = db.get(ruv)
        if not data:
            return dict(), 404
        data["events"] = db.get_audit(ruv)
        return jsonify(data), 200


@users_blueprint.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return jsonify({"error": original_error.message}), 400
    # handle other "Bad Request"-errors
    return error

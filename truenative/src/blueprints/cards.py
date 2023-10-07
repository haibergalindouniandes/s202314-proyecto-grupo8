from jsonschema import ValidationError
from flask import request, jsonify, Blueprint
from flask_expects_json import expects_json

from controllers.cards_controller import create_task, get_task
from db import DatabaseClient
from utils import validate_token
from errors import TransactionAlreadyRequested, NoHeaderToken, InvalidToken


SCHEMA = {
    "type": "object",
    "properties": {
        "transactionIdentifier": {"type": "string"},
        "card": {
            "type": "object",
            "properties": {
                "cardNumber": {"type": "string"},
                "cvv": {"type": "string"},
                "expirationDate":  {"type": "string"},
                "cardholderName":  {"type": "string"},
            }
        }
    },
    "required": ["transactionIdentifier", "card"]
}

cards_blueprint = Blueprint("cards", __name__)


@cards_blueprint.route("/native/cards", methods=["POST"])
@expects_json(SCHEMA)
def verify():
    try:
        if request.method == "POST":
            validate_token(request.headers)
            transaction_id = request.json["transactionIdentifier"]
            card = request.json["card"]
            data = create_task(transaction_id, card)
            return jsonify(data), 201
    except TransactionAlreadyRequested as err:
        return jsonify({"error": str(err)}), 409
    except InvalidToken:
        return jsonify({"error": "Token is required"}), 403
    except NoHeaderToken:
        return jsonify({"error": "Invalid token"}), 401


@cards_blueprint.route("/native/cards/<ruv>", methods = ["GET"])
def verify_ruv(ruv):
    try:
        if request.method == "GET":
            validate_token(request.headers)
            data = get_task(ruv)
            if not data:
                return dict(), 202
            return data, 200
    except InvalidToken:
        return jsonify({"error": "Token is required"}), 403
    except NoHeaderToken:
        return jsonify({"error": "Invalid token"}), 401


@cards_blueprint.route("/native/cards/log", methods = ["GET", "DELETE"])
def verify_log():
    db = DatabaseClient("cards")
    if request.method == "GET":
        data = db.get_all()
        return jsonify(data), 200
    if request.method == "DELETE":
        db.clean()
        return dict(), 200


@cards_blueprint.route("/native/cards/log/<ruv>", methods = ["GET"])
def verify_log_detail(ruv):
    if request.method == "GET":
        db = DatabaseClient("cards")
        data = db.get(ruv)
        if not data:
            return dict(), 404
        data["events"] = db.get_audit(ruv)
        return jsonify(data), 200


@cards_blueprint.errorhandler(400)
def bad_request(error):
    if isinstance(error.description, ValidationError):
        original_error = error.description
        return jsonify({"error": original_error.message}), 400
    # handle other "Bad Request"-errors
    return error

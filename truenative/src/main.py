import logging
logging.basicConfig(level=logging.INFO)

from flask import Flask, request
from environment import (
    SECRET_TOKEN,
    SUCCESS_RATE,
    MAX_POLL_DELAY,
    MAX_WEBHOOK_DELAY,
    set_env_var,
    get_poll_delay,
    get_secret_token,
    get_success_rate,
    get_webhook_delay
)

from blueprints.users import users_blueprint
from blueprints.cards import cards_blueprint


app = Flask(__name__)
app.register_blueprint(users_blueprint)
app.register_blueprint(cards_blueprint)


@app.route("/native/ping", methods = ["GET"])
def health_check():
    return "pong", 200


@app.route("/native/env", methods = ["POST", "GET"])
def set_env():
    if request.method == "POST":
        env_vars = [SECRET_TOKEN, SUCCESS_RATE, MAX_POLL_DELAY, MAX_WEBHOOK_DELAY]
        for var in env_vars:
            value = request.json.get(var)
            logging.info("%s was updated with value %s" % (var, value))
            if value is not None:
                set_env_var(var, value)
        return dict(), 200

    if request.method == "GET":
        return {
            SECRET_TOKEN: get_secret_token(),
            SUCCESS_RATE: get_success_rate(),
            MAX_POLL_DELAY: get_poll_delay(),
            MAX_WEBHOOK_DELAY: get_webhook_delay()
        }

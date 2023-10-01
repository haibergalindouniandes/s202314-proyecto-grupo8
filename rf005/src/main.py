# Importación de dependencias
from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from blueprints.resources import rf05_blueprint
from errors.errors import ApiError
#from models.models import db
import os

# Constantes
#DB_USER = os.environ["DB_USER"]
#DB_PASSWORD = os.environ["DB_PASSWORD"]
#DB_HOST = os.environ["DB_HOST"]
#DB_PORT = os.environ["DB_PORT"]
#DB_NAME = os.environ["DB_NAME"]
ROUTES_PATH = os.environ["ROUTES_PATH"]
OFFERS_PATH = os.environ["OFFERS_PATH"]
POSTS_PATH = os.environ["POSTS_PATH"]
USERS_PATH = os.environ["USERS_PATH"]
SCORES_PATH = os.environ["SCORES_PATH"]
APP_PORT =  int(os.getenv("APP_PORT", default=3000))


# Configuracion app
app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.register_blueprint(rf05_blueprint)
app_context = app.app_context()
app_context.push()
cors = CORS(app)
#db.init_app(app)
#db.create_all()
api = Api(app)

# Manejador de errores
@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
        "msg": err.description,
    }
    return jsonify(response), err.code

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=APP_PORT)
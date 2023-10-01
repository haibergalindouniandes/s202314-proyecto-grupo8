# Importación de dependencias
from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS
from blueprints.resources import rf004_blueprint
from errors.errors import ApiError
import os

# Constantes
APP_PORT =  int(os.getenv("APP_PORT", default=3000))

# Configuracion app
app = Flask(__name__)
app.register_blueprint(rf004_blueprint)
app_context = app.app_context()
app_context.push()
cors = CORS(app)
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

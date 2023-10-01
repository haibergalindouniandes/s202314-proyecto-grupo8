from models import create_app
from models.model import db
from models.config import set_config
from blueprints.api import api_blueprint
from flask_cors import CORS
from errors.errors import ApiError
from flask import jsonify
import os


APP_PORT =  int(os.getenv("APP_PORT", default=3000))

app = create_app()
set_config(app)
app_context = app.app_context()
app_context.push()
app.register_blueprint(api_blueprint)
cors = CORS(app)
db.init_app(app)
db.create_all()


@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
        "msg": err.description,
    }
    return jsonify(response), err.code



if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0", port=APP_PORT)

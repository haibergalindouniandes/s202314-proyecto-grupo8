from flask import Blueprint
from flask_restful import Api
from blueprints.vistas import VistaPosts, VistaPostsReset, VistaPost, VistaPostHealthCheck


api_blueprint = Blueprint('vistas', __name__)
api = Api(api_blueprint)
api.add_resource(VistaPosts, '/posts')
api.add_resource(VistaPostsReset, '/posts/reset')
api.add_resource(VistaPostHealthCheck, '/posts/ping')
api.add_resource(VistaPost, '/posts/<string:postId>')
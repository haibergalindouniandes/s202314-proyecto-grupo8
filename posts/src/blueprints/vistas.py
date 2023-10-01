from flask_restful import Resource
from flask import request, jsonify
from commands import create, delete, get, query, reset
from models.model import PostSchema
from validators.validators import validateToken



publicacion_schema = PostSchema()

class VistaPosts(Resource):

    def post(self):        
        userId = validateToken(request.headers)
        newPostObj = create.CreatePost(post_request_json=request.get_json(), userId=userId)
        new_post = newPostObj.execute()           
        return publicacion_schema.dump(new_post), 201


    def get(self):        
        userId = validateToken(request.headers)
        PostQueryObj = query.QueryPost(post_request_args=request.args, userId=userId)
        posts = PostQueryObj.execute()
        return [publicacion_schema.dump(post) for post in posts], 200


class VistaPostsReset(Resource):

    def post(self): 
        reset.ResetPosts().execute()        
        return jsonify({'msg': 'Todos los datos fueron eliminados'})


class VistaPost(Resource):

    def get(self, postId):
        validateToken(request.headers)
        PostGetObj = get.GetPost(postId=postId)
        post = PostGetObj.execute()
        return publicacion_schema.dump(post), 200

    def delete(self, postId):
        validateToken(request.headers)
        PostDeleteObj = delete.DeletePost(postId=postId)
        PostDeleteObj.execute()
        return jsonify({'msg': 'la publicación fue eliminada'})        
       

class VistaPostHealthCheck(Resource):
    def get(self):
        return "pong"
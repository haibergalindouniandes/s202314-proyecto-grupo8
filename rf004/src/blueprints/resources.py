import json
from flask import request, Blueprint, Response
from commands.create import CreateOffer
from validators.validators import validateToken


rf004_blueprint = Blueprint('rf004', __name__)

# Recurso que expone la funcionalidad healthcheck
@rf004_blueprint.route('/rf004/ping', methods=['GET'])
def health():
    return "pong"

# Recurso que expone la funcionalidad creacion de ofertas
@rf004_blueprint.route('/rf004/posts/<string:postId>/offers', methods=['POST'])
def create(postId):
    validateToken(request.headers)
    newOfferObj = CreateOffer(postId=postId, post_request_json=request.get_json(), headers=request.headers)
    offer_resp, score_resp = newOfferObj.execute()          
    if offer_resp.status_code == 201:
        data = {"id": offer_resp.json()["id"], "userId": offer_resp.json()["userId"], "createdAt": offer_resp.json()["createdAt"], "postId": postId}
        resp = Response(response=json.dumps({"data": data, "msg": {"score": score_resp.json()["score"]}}), status=201, mimetype='application/json')
    else:
        resp = Response(response=json.dumps({"data": {}, "msg": offer_resp.reason}, status=offer_resp.status_code), mimetype='application/json')    
    return resp
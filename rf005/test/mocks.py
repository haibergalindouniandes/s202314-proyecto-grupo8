from httmock import HTTMock, all_requests, urlmatch
from uuid import uuid4
from datetime import datetime, timedelta
from test.testmodels.models import Score, Offer
from flask.json import jsonify
import json




@urlmatch(path=r"/scores/posts/.*", method="GET")
def mock_post_scores_success(url, request):
    miLista = []
    newScore = Score(
        createdAt= f"{str(datetime.today()).split('.')[0].replace(' ', 'T')}.214Z",
        id= f"{uuid4()}",
        isPackageFragile= "False",
        offerAmount= "43.36",
        offerId= "7db2089e-51e7-11ee-a25b-0242ac120005",
        packageAmount= "21.28",
        packageDescription=  "consequatur corrupti eos",
        packageSize= "SMALL",
        postId="a66afbbc-7347-4e8d-b849-95f35a584ce3",
        score="38.45",
        userId= "ddb14b0f-bba1-41af-bace-a59b310483a5"
        )
    miLista.append(newScore.__dict__)
    return {
        "status_code": 200,
        "content": miLista
    }




@urlmatch(path=r".*offers.*", method="GET")
def mock_post_offers_success(url, request):
    miLista = []
    newOffer = Offer(
            id= "7db2089e-51e7-11ee-a25b-0242ac120005",
            postId= "a66afbbc-7347-4e8d-b849-95f35a584ce3",
            description= "Oferta 1",
            size= "SMALL",
            fragile= "TRUE",
            offer= "21.25",
            createdAt= "023-09-20T03:41:58.272000",#f"{str(datetime.today() + timedelta(days=1)).split('.')[0].replace(' ', 'T')}.214Z",
            userId= "ddb14b0f-bba1-41af-bace-a59b310483a5"
    )
    miLista.append(newOffer.__dict__)
    
    return {
        "status_code": 200,
        "content":miLista,
        
    }



@urlmatch(path=r".*routes/.*", method="GET")
def mock_post_route_success(url, request):
    return {
        "status_code": 200,
        "content": {
            "id": "a66afbbc-7347-4e8d-b849-95f35a584ce3",
            "flightId": "889",
            "sourceAirportCode": "BOG",
            "sourceCountry": "Colombia",
            "destinyAirportCode": "MDE",
            "destinyCountry": "Mexico",
            "bagCost": 123,
            "plannedStartDate": f"{str(datetime.today() + timedelta(days=1)).split('.')[0].replace(' ', 'T')}.214Z",
            "plannedEndDate": f"{str(datetime.today() + timedelta(days=10)).split('.')[0].replace(' ', 'T')}.214Z",
            "createdAt": f"{str(datetime.today()).split('.')[0].replace(' ', 'T')}.214Z",
        },
    }



@urlmatch(path=r".*users/me.*", method="GET")
def mock_post_users_success(url, request):
    return {
        "status_code": 200,
        "content": {
            "dni":"573",
            "email":"edwina72@hotmail.com",
            "fullName":"kelly kuvalis phd",
            "id":"ddb14b0f-bba1-41af-bace-a59b310483a5",
            "phoneNumber":"4484535552",
            "status":"NO_VERIFICADO",
            "username":"ray"
        },
    }



@urlmatch(path=r"/posts.*", method="GET")
def mock_post_rf005_success(url, request):
    return {
        "status_code": 200,
        "content": {
            "id": "7db2089e-51e7-11ee-a25b-0242ac120005",
            "routeId": "a66afbbc-7347-4e8d-b849-95f35a584ce3",
            "userId": "ddb14b0f-bba1-41af-bace-a59b310483a5",
            "createdAt": "2023-09-13T03:41:58.317925",
            "expireAt": "2023-09-20T03:41:58.272000"
            },
    }

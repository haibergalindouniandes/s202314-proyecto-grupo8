from httmock import HTTMock, all_requests, urlmatch
from uuid import uuid4
from datetime import datetime, timedelta


@urlmatch(path=r".*users/me")
def mock_success_auth(url, request):
    return {"status_code": 200, "content": {"id": f"uuid4()"}}


@urlmatch(path=r".*users/me")
def mock_failed_auth(url, request):
    return {"status_code": 401}


@urlmatch(path=r".*users/me")
def mock_forbidden_auth(url, request):
    return {"status_code": 403}


@urlmatch(path=r".*routes.*", method="GET")
def mock_query_route_empty(url, request):
    return {"status_code": 200, "content": []}


@urlmatch(path=r".*posts*", method="GET")
def mock_user_post_route_success(url, request):
    return {"status_code": 200, "content": []}


@urlmatch(path=r".*routes.*", method="POST")
def mock_post_route_error(url, request):
    return {"status_code": 412}


@urlmatch(path=r".*routes.*", method="POST")
def mock_post_route_success(url, request):
    return {
        "status_code": 201,
        "content": {
            "id": f"uuid4()",
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

@urlmatch(path=r".*posts*", method="POST")
def mock_post_create_success(url, request):
    return {
        "status_code": 201,
        "content": {
            "id": f"uuid4()",
            "userId": f"uuid4()",
            "createdAt": f"{str(datetime.today()).split('.')[0].replace(' ', 'T')}.214Z",
        },
    }

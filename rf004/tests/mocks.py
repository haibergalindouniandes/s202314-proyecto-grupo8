from httmock import urlmatch, response
from uuid import uuid1



@urlmatch(path=r".*users/me")
def mock_success_auth(url, request):
    return response(status_code=200, content={"id": str(uuid1())})
    

@urlmatch(path=r".*users/me")
def mock_failed_auth(url, request):
    return response(status_code=401)


@urlmatch(path=r".*users/me")
def mock_forbidden_auth(url, request):
    return response(status_code=403)


@urlmatch(path=r".*posts*", method="GET")
def mock_post_expired(url, request):
    if url.query=='expire=true':
       return response(status_code=412, content=[{"id":"db29e615-4f25-11ee-99f7-c89402273298"}])
            

@urlmatch(path=r".*posts*", method="GET")
def mock_post_invalid_owner(url, request):
    if url.query=='owner=me':
        return response(status_code=413, content=[{"id":"41f37778-5201-11ee-839c-c89402273298"}]) 


@urlmatch(path=r".*posts*", method="GET")
def mock_post_invalid_id(url, request):    
    if url.path=='/posts/12345':
        return response(status_code=404, content=[]) 


@urlmatch(path=r".*posts*", method="GET")
def mock_post_id_doesnt_exist(url, request):    
    if url.path=='/posts/8c749f81-5205-11ee-b059-c89402273298':
        return response(status_code=404, content=[])

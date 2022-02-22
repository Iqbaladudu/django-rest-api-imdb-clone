from rest_framework.request import Request

def GET(request: Request) -> bool:
    return request.method == 'GET'


def POST(request: Request) -> bool:
    return request.method == 'POST'


def PUT(request: Request) -> bool:
    return request.method == 'PUT'


def DELETE(request: Request) -> bool:
    return request.method == 'DELETE'
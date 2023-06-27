from django.http import JsonResponse

import json


def api_home(request, *args, **kwargs):
    return JsonResponse({
        'status': 'success',
        'message': 'Welcome to the API!'
    })


def api_echo(request, *args, **kwargs):
    body = request.body
    print(body)
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    # data['headers'] = request.headers
    data['content_type'] = request.content_type
    print(data)
    return JsonResponse(data)

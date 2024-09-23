from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def api_response(request):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(request.headers)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    data["parameters"] = request.GET
    return JsonResponse(data)
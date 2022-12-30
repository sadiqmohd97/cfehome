from django.shortcuts import render
from django.http import JsonResponse,HttpRequest
import json

# Create your views here.
 
def index(request:HttpRequest):
    print(request)
    body = request.body  #byte string of json
    data = {}
    print(request.GET) #QueryDict
    data['params'] = request.GET
    try:
        data = json.loads(body) #dictionary
    except:
        pass
    print(data)
    print(type(data))
    print(data.keys())
    data['params'] = request.GET
    data['headers'] = dict(request.headers)
    data['content-type'] = request.content_type
    return JsonResponse(data) 

  
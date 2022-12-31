from django.shortcuts import render
from django.http import JsonResponse

from .models import Product
import json
from django.forms.models import model_to_dict
# Create your views here.

def api_home(request,*args, **kwargs):
    model_data = Product.objects.all().first()
    # return JsonResponse(model_to_dict(model_data))
    print(type(model_data))
    data = {}
    if model_data:
        print('exists')
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['price'] = model_data.price
        json_data =  model_to_dict(model_data)
    else:
        print('Doesn')
        print(model_data.count())

    return JsonResponse(json_data)

def get_all_products(request,*args, **kwargs):
    res = {}
    products = Product.objects.all()
    res['products'] = [model_to_dict(p) for p in products]
    return JsonResponse(res)
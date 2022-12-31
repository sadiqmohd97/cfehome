from django.shortcuts import render
from django.http import JsonResponse, HttpResponse , HttpRequest
from django.views.decorators.csrf import csrf_exempt
import time

from .serializers import ProductSerializer

from .models import Product
import json
from django.forms.models import model_to_dict

from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import generics, mixins
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

@api_view(['GET'])
def get_all_products(request,*args, **kwargs):
    res = {}
    products = Product.objects.all()
    #res['products'] = [model_to_dict(p) for p in products]
    instances = ProductSerializer(products.first()).data
    #instances.update({"title":"Updated"})
    return Response(instances)


# using rest-framework

@api_view(['GET'])
def get_products(request,*args, **kwargs):
    instance = Product.objects.all().first()
    data = {}
    if instance:
        data = ProductSerializer(instance).data
        #data = model_to_dict(products,fields=['id','title','price','sale_price'])
        #print(data)
        #print("Sale Price" ,products.sale_price)
    return Response(data)

@api_view(['POST'])  
def save_product(request:HttpRequest,*args, **kwargs):
    data = request.data
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print('instance after save()',instance)
        print('type is',type(instance))
        print('Valid Data')
    else:
        print("Invalid Data")
    print(data)
    print(type(data))
    return JsonResponse(serializer.data)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'



class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer:ProductSerializer):
        title = serializer.validated_data.get('title') + str(time.time())
        serializer.save(title = title)


class ProductListAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer:ProductSerializer):
        old_obj = self.queryset.get(pk=14)      
        instance = serializer.save()
        data = {
            'old_data' : ProductSerializer(old_obj).data,
            'new_data' : serializer.data       
             }
        print("Comparison") 
        print(data)    
        

class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


    def perform_destroy(self, instance:Product):
        print(instance)
        return super().perform_destroy(instance)
    

# class based views

class ProductMixinView( mixins.ListModelMixin, generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self,request,*args, **kwargs):
        print(args,kwargs)
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request,*args, **kwargs)
        else:
            return self.list(request,*args, **kwargs) 
    
    def post(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)






        



    

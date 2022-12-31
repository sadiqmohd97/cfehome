from django.urls import path
from .views import api_home,get_all_products

urlpatterns = [
    path("all",api_home),
    path('get',get_all_products)
]


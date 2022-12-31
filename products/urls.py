from django.urls import path
from .views import api_home,get_all_products,get_products, save_product,ProductDetailAPIView,ProductCreateAPIView,ProductListAPIView,ProductUpdateAPIView,ProductDestroyAPIView

urlpatterns = [
    path("",ProductListAPIView.as_view()),
    path("all",get_all_products),
    path('get',get_products),
    path('save',save_product),
    path('<int:id>/',ProductDetailAPIView.as_view()),
    path('create', ProductCreateAPIView.as_view()),
    path('update/<int:pk>',ProductUpdateAPIView.as_view()),
    path('delete/<int:pk>',ProductDestroyAPIView.as_view())
]


from django.urls import path,include
from .views import (api_home,get_all_products,get_products, save_product,ProductDetailAPIView,
                ProductCreateAPIView,ProductListAPIView,ProductUpdateAPIView,ProductDestroyAPIView,
                ProductMixinView
                )

urlpatterns = [
    path("",ProductListAPIView.as_view(),name='product-list'),
    path("all",get_all_products),
    path('get',get_products),
    path('save',save_product),
    path('<int:pk>/',ProductDetailAPIView.as_view(),name='product-detail'),
    path('create', ProductCreateAPIView.as_view()),
    path('update/<int:pk>',ProductUpdateAPIView.as_view()),
    path('delete/<int:pk>',ProductDestroyAPIView.as_view()),
    path('mixin/all/<int:pk>',ProductMixinView.as_view()),
    path('mixin/all',ProductMixinView.as_view()),
    path('mixin/delete/<int:pk>',ProductMixinView.as_view()),
]


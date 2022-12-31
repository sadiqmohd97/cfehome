from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'id',
            'title', 
            'price',
            'content',
            'sale_price', 
            'my_discount',
            'category'
        ]

    def get_my_discount(self,obj:Product): 
        print(obj)
        try:
            return obj.get_discount()
        except:
            return None

           
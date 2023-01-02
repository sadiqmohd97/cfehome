from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    urls = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field = 'pk'
    )
    class Meta:
        model = Product
        fields = [
            'id',
            'title', 
            'price',
            'content',
            'sale_price', 
            'my_discount',
            'category',
            'edit_url'
        ]

    def get_edit_url(self,obj):
        #return f"products/all/{obj.pk}"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-detail",kwargs={"pk":obj.pk},request=request)

    def get_my_discount(self,obj:Product): 
        print(obj)
        try:
            return obj.get_discount()
        except:
            return None

           
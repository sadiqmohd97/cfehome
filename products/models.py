from django.db import models
import random

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=15,decimal_places=2,default=99.99)

    @property
    def sale_price(self):
        return "%.2f" %(float(self.price) * 0.8)

    @property
    def category(self):
        cats = ['Electronic','Clothing','Furniture','Random']
        return random.choice(cats)


    def get_discount(self):
        return (float(self.price) -float(self.sale_price))


    def __str__(self) -> str:
        return self.title
from django.contrib import admin
from .models import Loan,Customer,Provider,ProviderConfig

# Register your models here.


admin.site.register(Loan)
admin.site.register(Provider)
admin.site.register(Customer)
admin.site.register(ProviderConfig)

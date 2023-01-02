from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    pan = models.CharField(max_length=10)
    email = models.EmailField(blank=True,null=True)
    phone_num =  models.CharField(max_length=15)
    address = models.CharField(max_length=200,null=True,blank=True)


    def __str__(self) -> str:
        return "Name : {} {}".format(self.first_name,self.last_name)


class ProviderConfig(models.Model):
    interest_rate = models.DecimalField(decimal_places=2,max_digits=5)
    penal_charge = models.FloatField()
    minimum_loan_amount = models.IntegerField()
    max_loan_amount = models.IntegerField(default=500000)

    def __str__(self) -> str:
        return "ROI {}".format(self.interest_rate)


class Provider(models.Model):
    name = models.CharField(max_length=100)
    config_id = models.ForeignKey(ProviderConfig,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name    
    

class Loan(models.Model):
    loan_id = models.AutoField(primary_key=True)
    principal_amount = models.FloatField()
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    provider_id = models.ForeignKey(Provider,on_delete=models.SET_NULL,null=True)
    tenure = models.IntegerField(default=12)
    start_date = models.DateField()
    closed_date = models.DateField(blank=True,null=True)

    def __str__(self) -> str:
        return "{} {} Customer Id {} Provider Id {}".format(self.loan_id,self.principal_amount,self.customer_id,self.customer_id,self.provider_id)
    

    

    
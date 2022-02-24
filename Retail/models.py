from django.db import models
from Jobs.models import *

class Payment_type(models.Model):
    payment = models.CharField(max_length=250, null = True, blank=True)

    def __str__(self):
        return self.payment
    


class Customer_cart(models.Model):
    c_cart = models.ForeignKey(Jobs, on_delete = models.CASCADE, null=True, blank=True)
    deliver_cost = models.CharField(max_length=250, null = True, blank=True)
    payment_type = models.ForeignKey(Payment_type,  on_delete=models.CASCADE, null = True, blank=True)
    reciept = models.ForeignKey(Reciepts,  on_delete=models.CASCADE, null = True, blank=True)
    sale_person = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

    

    def get_make(self):
        return self.c_cart.make

    def get_imei(self):
        return self.c_cart.imei

    def get_model(self):
        return self.c_cart.model

    def get_job_id(self):
        return self.c_cart.id


class Daily_sale(models.Model):
    d_sale = models.ForeignKey(Customer_cart, on_delete = models.CASCADE, null=True, blank=True)

    #payment_reciept = models.ForeignKey(Reciepts,  on_delete=models.CASCADE, null = True, blank=True)
    sale_person = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.d_sale.id)
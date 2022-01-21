from django.db import models
from customer.models import *



class Devices(models.Model):
    customer =models.ForeignKey(Customer,on_delete=models.CASCADE)
    devices = models.CharField(max_length=250)

    def __str__(self):
        return self.devices

class Make(models.Model):
    device = models.ForeignKey(Devices,on_delete=models.CASCADE)
    make = models.CharField(max_length=250)

    def __str__(self):
        return self.make

class Model(models.Model):
    make = models.ForeignKey(Make,on_delete=models.CASCADE) 
    model = models.CharField(max_length=250)
    imei = models.CharField(max_length=250)

    def __str__(self):
        return self.model
from django.db import models
import datetime


class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone  = models.IntegerField()
    landline  = models.IntegerField()
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250)
    postcode = models.CharField(max_length=250)
    created_date = models.DateTimeField(null=True, blank= True)#

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


from django.db import models
from customer.models import *
from django.contrib.auth.models import User



class Devices(models.Model):
    customer =models.ForeignKey(Customer,on_delete=models.CASCADE)
    devices = models.CharField(max_length=250)

    def __str__(self):
        return self.devices

    def get_id(self):
        return self.id # with this function we can call specific ID for devices column

class Make(models.Model):
    device = models.ForeignKey(Devices,on_delete=models.CASCADE, related_name='make_device')
    make = models.CharField(max_length=250)

    def __str__(self):
        return self.make

    def get_make_id(self):
        return self.id # with this functuon we can call specific ID for Make column

class Model(models.Model):
    make = models.ForeignKey(Make,on_delete=models.CASCADE) 
    model = models.CharField(max_length=250)


    def __str__(self):
        return self.model

PAYMENT_STATUS = (
    ('PAID', 'PAID'),
    ('UNPAID', 'UNPAID'),
    ('CREDIT NOTE', 'CREDIT NOTE'),
    ('REFUND', 'REFUND')
    

)

class Fault(models.Model):
    fault =  models.CharField(max_length=250)

    def __str__(self):
        return self.fault



class Accessories(models.Model):
    accessories =  models.CharField(max_length=250)

    def __str__(self):
        return self.accessories

class Sale_item(models.Model):
    sale_item =  models.CharField(max_length=250)

    def __str__(self):
        return self.sale_item

class Network(models.Model):
    network =  models.CharField(max_length=250)

    def __str__(self):
        return self.network


class Job_status(models.Model):
    job_status =  models.CharField(max_length=250)

    def __str__(self):
        return self.job_status

# class Payment_status(models.Model):
#     payment_status =  models.CharField(max_length=250)

#     def __str__(self):
#         return self.payment_status




class Jobs(models.Model):
    
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE, related_name = 'job_customer')
    device =  models.ForeignKey(Devices,on_delete = models.CASCADE, related_name = 'job_device', null = True, blank=True)
    make = models.ForeignKey(Make,on_delete = models.CASCADE, related_name = 'job_make')
    model = models.ForeignKey(Model,on_delete = models.CASCADE, related_name = 'job_model')
    fault =  models.ForeignKey(Fault,on_delete = models.CASCADE, related_name = 'job_faults')
    description = models.TextField()
    imei = models.CharField(max_length=250)
    accessories = models.ForeignKey(Accessories,on_delete = models.CASCADE, related_name = 'job_acessories')
    sale_item = models.ForeignKey(Sale_item,on_delete = models.CASCADE, related_name = 'job_acessories')
    passcode = models.CharField(max_length=250)
    network = models.ForeignKey(Network,on_delete = models.CASCADE, related_name = 'job_network')
    cost = models.IntegerField()
    job_status = models.ForeignKey(Job_status,on_delete = models.CASCADE, related_name = 'job_job_status')
    collection_time = models.DateTimeField()
    payment_status = models.CharField(choices= PAYMENT_STATUS, max_length=250)
    created_date = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)



    def __str__(self):
        return self.model.model



class Job_update(models.Model):

    job = models.ForeignKey(Jobs,on_delete = models.CASCADE, related_name = 'job_update')
    description_update = models.TextField()
    updated_on = models.DateTimeField(null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.job.device.devices

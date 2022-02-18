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

TEST_ALL_FUNCTIONS = (
    ('MIC', 'MIC'),
    ('SCREEN', 'SCREEN'),
    ('HEARING SPEAKER', 'HEARING SPEAKER'),
    ('LOUD SPEAKER', 'LOUD SPEAKER'),
    ('WIFI', 'WIFI')
    
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
        return str(self.id)



class Job_update(models.Model):

    job_update = models.ForeignKey(Jobs,on_delete = models.CASCADE, related_name = 'job_update' , null = True, blank=True)
    customer_update = models.ForeignKey(Customer,on_delete = models.CASCADE, related_name = 'customer_update', null = True, blank=True)
    device_update =  models.ForeignKey(Devices,on_delete = models.CASCADE, related_name = 'device_update', null = True, blank=True)
    make_update = models.ForeignKey(Make,on_delete = models.CASCADE, related_name = 'make_update', null = True, blank=True)
    model_update = models.ForeignKey(Model,on_delete = models.CASCADE, related_name = 'model_update', null = True, blank=True)
    fault_update =  models.ForeignKey(Fault,on_delete = models.CASCADE, related_name = 'fault_update', null = True, blank=True)
    description_update = models.TextField(null = True, blank=True)
    imei_update = models.CharField(max_length=250, null = True, blank=True)
    accessories_update = models.ForeignKey(Accessories,on_delete = models.CASCADE, related_name = 'accessories_update', null = True, blank=True)
    sale_item_update = models.ForeignKey(Sale_item,on_delete = models.CASCADE, related_name = 'update_sale_item', null = True, blank=True)
    passcode_update = models.CharField(max_length=250, null = True, blank=True)
    network_update = models.ForeignKey(Network,on_delete = models.CASCADE, related_name = 'network_update', null = True, blank=True)
    cost_update = models.IntegerField(null = True, blank=True)
    job_status_update = models.ForeignKey(Job_status,on_delete = models.CASCADE, related_name = 'job_status_update', null = True, blank=True)
    collection_time_update = models.DateTimeField(null = True, blank=True)
    payment_status_update = models.CharField(choices= PAYMENT_STATUS, max_length=250, null = True, blank=True)
    updated_on = models.DateTimeField(null=True, blank=True)
    updated_by = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.job_update.id)


class Fingerprints(models.Model):
    user_fprint = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    date_time_fprint = models.CharField(max_length=250, null=True, blank=True)
    job_fprint = models.ForeignKey(Jobs,on_delete = models.CASCADE , null = True, blank=True)




class Reciepts(models.Model):
    reciept = models.ForeignKey(Jobs, on_delete = models.CASCADE, null=True, blank=True)



# class Contact_by_email(models.Model):
#     email = models.ForeignKey(Jobs, on_delete = models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return f'{self.email.id} {self.email.customer.first_name} {self.email.customer.email}'



TEST_ALL_FUNCTIONS = (
    ('MIC', 'MIC'),
    ('SCREEN', 'SCREEN'),
    ('HEARING SPEAKER', 'HEARING SPEAKER'),
    ('LOUD SPEAKER', 'LOUD SPEAKER'),
    ('WIFI', 'WIFI')
    
)

class Complete_job(models.Model):
    c_job = models.ForeignKey(Jobs, on_delete = models.CASCADE, null=True, blank=True)
    complete_update = models.TextField(null = True, blank=True)
    checked = models.BooleanField(default=False)
    completed_by = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        #return f'{self.c_job.id} {self.c_job.make} {self.c_job.make} '
        return self.complete_update

    
    
    


























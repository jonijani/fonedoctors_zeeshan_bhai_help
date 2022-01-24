from django.shortcuts import render
from customer.models import *
from .models import *
from django.http import HttpResponse


def add_job(request):
    customers = Customer.objects.all()
    device = Devices.objects.all()
    make = Make.objects.all()
    model = Model.objects.all()
    context = {'customers':customers,'device_context':device,  'make_context':make, 'model_context':model}
    return render(request,'add_job.html',context)
    

def dashboard(request):
    return render(request,'dashboard.html')



def search_job(request):
    return render(request,'search_job.html')

def job_created(request):
    return render(request,'job_created.html')




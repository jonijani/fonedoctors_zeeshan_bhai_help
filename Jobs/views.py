from django.shortcuts import render
from customer.models import *
from .models import *

def add_job(request):
    customers = Customer.objects.all()
    make = Make.objects.all()
    context = {'customers':customers, 'make_context':make}
    return render(request,'add_job.html',context)
    

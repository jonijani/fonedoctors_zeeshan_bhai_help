from django.shortcuts import render
from customer.models import *
from .models import *
from django.http import HttpResponse


def add_job(request):
    customers = Customer.objects.all()
    make = Make.objects.all()
    context = {'customers':customers, 'make_context':make}
    return render(request,'add_job.html',context)
    

def dashboard(request):
    return HttpResponse('you are in  dashboard')

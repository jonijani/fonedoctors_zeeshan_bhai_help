from django.shortcuts import render
from customer.models import *
from .models import *
from django.http import HttpResponse


def add_job(request):
    if request.method == "POST":
        customer = request.POST.get('customer')#customer in brackets comes from html Name = customer
        device = request.POST.get('device_mobile')
        make = request.POST.get('make')
        model = request.POST.get('model')
        imei = request.POST.get('imei')
        
    customers = Customer.objects.all()
    device = Devices.objects.all()
    make = Make.objects.all()
    model = Model.objects.all()
    fault = Fault.objects.all()
    accessories = Accessories.objects.all()
    sale_item = Sale_item.objects.all()
    network = Network.objects.all()

    context = {'customers':customers,'device_context':device, 
                 'make_context':make, 'model_context':model,
                 'fault_context':fault ,'accessories_context':accessories, 
                 'sale_item_context':sale_item , 'network_context':network}
    return render(request,'add_job.html',context)
    

def dashboard(request):
    return render(request,'dashboard.html')



def search_job(request):
    return render(request,'search_job.html')

def job_created(request):
    return render(request,'job_created.html')




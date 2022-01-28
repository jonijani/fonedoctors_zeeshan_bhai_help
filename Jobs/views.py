from django.shortcuts import render, redirect
from customer.models import *
from .models import *
from django.http import HttpResponse


def add_job(request):
    if request.method == "GET":
        customers = Customer.objects.all()
        device = Devices.objects.all()
        make = Make.objects.all()
        model = Model.objects.all()
        fault = Fault.objects.all()
        accessories = Accessories.objects.all()
        sale_item = Sale_item.objects.all()
        network = Network.objects.all()
        job_status = Job_status.objects.all()
        #payment = payment_status.objects.all()  'payment_status_context':payment,  
        context = {'customers':customers,
                    'device_context':device, 
                    'make_context':make, 
                    'model_context':model,
                    'fault_context':fault ,
                    'accessories_context':accessories, 
                    'sale_item_context':sale_item , 
                    'network_context':network,
                    'job_status_context': job_status
                    }
        return render(request,'add_job.html',context)
    
    if request.method == "POST":
    
        #bring all front end inputs to view so we can connect them with models.
        customer1 = request.POST.get('customer')#customer in brackets comes from html Name = customer
        device = request.POST.get('device_mobile')
        make = request.POST.get('make')
        model = request.POST.get('model')
        imei = request.POST.get('imei')
        fault = request.POST.get('faults')
        description = request.POST.get('description')
        accessories = request.POST.get('accessories')
        sale_item = request.POST.get('sale_item')
        passcode = request.POST.get('passcode')
        network = request.POST.get('network')
        cost = request.POST.get('cost')
        job_status = request.POST.get('job_status')
        eta = request.POST.get('eta')
        payment = request.POST.get('payment_status')

        customer_id = Customer.objects.get(id=customer1)
        device_id = Devices.objects.get(devices=device)
        make_id = Make.objects.get(make=make)
        model_id = Model.objects.get(model=model)
        fault_id = Fault.objects.get(fault=fault)
        acessories_id = Accessories.objects.get(accessories=accessories)
        sale_item_id = Sale_item.objects.get(sale_item=sale_item)
        network_id = Network.objects.get(network=network)
        job_status_id = Job_status.objects.get(job_status=job_status)

        data = Jobs(customer=customer_id,
                    device=device_id,
                    make=make_id,
                    model=model_id,
                    fault=fault_id,
                    description=description,
                    imei=imei,
                    accessories=acessories_id,
                    sale_item=sale_item_id,
                    passcode=customer_id,
                    network=network_id,
                    cost=cost,
                    job_status=job_status_id,
                    collection_time=eta,
                    payment_status=payment ).save()
        return redirect('job_created')            
    


                
            # #here we select customer and connect with add job form 
            # customer_var = Customer.objects.get(customer=customer1)
            # device_var = Devices(customer=customer_var, devices=device)# customer is variable comes from line 10 
            #                                                                 #and selected_customer is new variale in line 26
            #                                                                 #and devices is column/field from models class and device is variable in line 11.
                
            # make_var = Make(make=make)
            # model_var = Model(model=model)
            # fault_var = Fault(fault=fault)
            # description_var = Jobs(description=description)
            # accessories_var = Accessories(accessories=accessories)
            # sale_item_var = Sale_item(sale_item=sale_item)
            # passcode_var = Jobs(passcode=passcode)
            # network_var = Network(network=network)
            # cost_var = Jobs(cost=cost)
            # job_status_var = Job_status(job_status=job_status)
            # eta_var = Jobs(collection_time=eta)
            # payment_status_var = Jobs(payment_status=payment)

            # all_var = [customer_var, device_var, make_var , model_var, fault_var, description_var, accessories_var, sale_item_var, passcode_var, network_var, cost_var, job_status_var, eta_var, payment_status_var ]
            # all_var.save()
            
             
            

        
    

def dashboard(request):
    return render(request,'dashboard.html')



def search_job(request):
    return render(request,'search_job.html')

def job_created(request):
    return render(request,'job_created.html')




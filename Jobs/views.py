from django.shortcuts import render, redirect
from customer.models import *
from .models import *
from django.http import HttpResponse
import random
import datetime
from django.core.mail import send_mail


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

        customer_id = Customer.objects.get(id=customer1)# customer_id is new variable than Customer class and in brackets id comes from html value="id" and customer is variable in line 35.
        device_id = Devices.objects.get(devices=device)
        make_id = Make.objects.get(make=make)
        model_id = Model.objects.get(model=model)
        fault_id = Fault.objects.get(fault=fault)
        acessories_id = Accessories.objects.get(accessories=accessories)
        sale_item_id = Sale_item.objects.get(sale_item=sale_item)
        network_id = Network.objects.get(network=network)
        job_status_id = Job_status.objects.get(job_status=job_status)
        

        data = Jobs(customer=customer_id,#customer is column or field from classes and customer_id from line 51.
                    device=device_id,
                    make=make_id,
                    model=model_id,
                    fault=fault_id,
                    description=description,
                    imei=imei,
                    accessories=acessories_id,
                    sale_item=sale_item_id,
                    passcode=passcode,
                    network=network_id,
                    cost=cost,
                    job_status=job_status_id,
                    collection_time=eta,
                    payment_status=payment,
                    created_by = request.user,
                    created_date = datetime.datetime.now() )
        data.save() 
        job_data =  Jobs.objects.get(id=data.id)          
        reciept = Reciepts(reciept=job_data)
        reciept.save()

        return redirect('reciept',data.id) 



def add_direct_job(request,id):
    if request.method == "GET":
        customers = Customer.objects.get(id=id)
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
        return render(request,'add_direct_job.html',context)
    
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

        customer_id = Customer.objects.get(id=customer1)# customer_id is new variable than Customer class and in brackets id comes from html value="id" and customer is variable in line 108.
        device_id = Devices.objects.get(devices=device)
        make_id = Make.objects.get(make=make)
        model_id = Model.objects.get(model=model)
        fault_id = Fault.objects.get(fault=fault)
        acessories_id = Accessories.objects.get(accessories=accessories)
        sale_item_id = Sale_item.objects.get(sale_item=sale_item)
        network_id = Network.objects.get(network=network)
        job_status_id = Job_status.objects.get(job_status=job_status)
        job_created_date = datetime.datetime.now() #craeted new variable to store current time ( datetime.datetime.now())
        job_created_by = request.user

        data = Jobs(customer=customer_id,#customer is column or field from classes and customer_id from line 51.
                    device=device_id,
                    make=make_id,
                    model=model_id,
                    fault=fault_id,
                    description=description,
                    imei=imei,
                    accessories=acessories_id,
                    sale_item=sale_item_id,
                    passcode=passcode,
                    network=network_id,
                    cost=cost,
                    job_status=job_status_id,
                    collection_time=eta,
                    payment_status=payment,
                    created_date= job_created_date,
                    created_by=job_created_by )
        
               
        data.save() 
        job_data =  Jobs.objects.get(id=data.id)          
        reciept = Reciepts(reciept=job_data)
        reciept.save()           
        job = Jobs.objects.get(id=data.id)#here we fetch last job added and show to user
        context = {'job_created_context':job}            
        return render(request, 'job_created.html', context)
    
            
             
    

def dashboard(request):
    return render(request,'dashboard.html')



def search_job(request):
    return render(request,'search_job.html')



def job_detail_page(request,id):
    detail_page = Jobs.objects.get(id=id)
    job_update_table = Job_update.objects.filter(job_update=id)
    now = datetime.datetime.now()
    Fprint = Fingerprints.objects.filter(job_fprint=id)# job_fprint comes from models as its related to that specific job
    update_finger_print= Fingerprints(user_fprint=request.user, date_time_fprint=now.strftime("%m/%d/%Y, %H:%M:%S"), job_fprint=detail_page)
    update_finger_print.save()
    context = {'detail_page_context':detail_page, 'job_update_table_context':job_update_table, 'Fprint_context':Fprint }
    return render(request,'job_detail_page.html',context)



def job_update_page(request,id):
    job_update = Jobs.objects.get(id=id)
    customers = Customer.objects.get(id=id)
    device = Devices.objects.all()
    make = Make.objects.all()
    model = Model.objects.all()
    fault = Fault.objects.all()
    accessories = Accessories.objects.all()
    sale_item = Sale_item.objects.all()
    network = Network.objects.all()
    job_status = Job_status.objects.all()
    #payment = payment_status.objects.all()  'payment_status_context':payment,  
        
    if request.method == "POST":
        #customer1 = request.POST.get('customer')#customer in brackets comes from html Name = customer
        #device = request.POST.get('device_mobile')
        #make = request.POST.get('make')
        #model = request.POST.get('model')
        imei = request.POST.get('imei_update')
        fault = request.POST.get('fault_update')
        description = request.POST.get('description_update')
        accessories = request.POST.get('accessories_update')
        sale_item = request.POST.get('sale_item_update')
        passcode = request.POST.get('passcode_update')
        network = request.POST.get('network_update')
        cost = request.POST.get('cost_update')
        job_status = request.POST.get('job_status_update')
        eta = request.POST.get('eta_update')
        payment = request.POST.get('payment_status_update')

        #customer_id = Customer.objects.get(id=customer1)# customer_id is new variable than Customer class and in brackets id comes from html value="id" and customer is variable in line 108.
        #device_id = Devices.objects.get(devices=device)
        #make_id = Make.objects.get(make=make)
        #model_id = Model.objects.get(model=model)
        fault_id = Fault.objects.get(fault=fault)
        acessories_id = Accessories.objects.get(accessories=accessories)
        sale_item_id = Sale_item.objects.get(sale_item=sale_item)
        network_id = Network.objects.get(network=network)
        job_status_id = Job_status.objects.get(job_status=job_status)
        job_created_date = datetime.datetime.now() #craeted new variable to store current time ( datetime.datetime.now())
        job_created_by = request.user
        job_update_data = Jobs.objects.get(id=id)

        data = Job_update(
                    job_update = job_update_data,
                    fault_update=fault_id,
                    description_update=description,
                    imei_update=imei,
                    accessories_update=acessories_id,
                    sale_item_update=sale_item_id,
                    passcode_update=passcode,
                    network_update=network_id,
                    cost_update=cost,
                    job_status_update=job_status_id,
                    collection_time_update=eta,
                    payment_status_update=payment,
                    updated_on= job_created_date,
                    updated_by=job_created_by )
        
               
        data.save()
        return redirect('job_detail_page',id=id)
    context = {'customers':customers,
                    'device_context':device, 
                    'make_context':make, 
                    'model_context':model,
                    'fault_context':fault ,
                    'accessories_context':accessories, 
                    'sale_item_context':sale_item , 
                    'network_context':network,
                    'job_status_context': job_status,
                    'job_update_context':job_update
                    
                    }
    
    return render(request,'job_update_page.html', context)





def reciept(request,id):
    reciept = Reciepts.objects.filter(reciept=id)
    context = {'reciept':reciept}
    return render(request,'reciept.html',context)


def send_email_page(request,id, reciept_id):
    customer = Customer.objects.get(id=id)
    job = Jobs.objects.get(id=reciept_id)
    send_mail(
    'hello please find your reciept',
    f'{job.id} {job.device} {job.make} {job.model} {job.imei}  {job.fault} {job.cost} {job.payment_status} {job.payment_status} {job.created_by}',
    'learningdjango1@gmail.com',
    [customer.email],
    fail_silently=True,
)
    return render(request,'send_email_page.html')

    

def send_text_page(request):
    return render(request,'send_text_page.html')




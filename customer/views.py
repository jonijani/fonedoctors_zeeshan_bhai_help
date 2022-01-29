from django.shortcuts import render, redirect
from .models import Customer
import datetime
from django.http import HttpResponse


def home(request):
    return render(request,'login.html')

def add_customer(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone = request.POST.get('phone')
        landline = request.POST.get('landline')
        email = request.POST.get('email')
        address = request.POST.get('address')
        postcode = request.POST.get('postcode')
        created_date = datetime.datetime.now()
        created_by = request.user
        data = Customer(first_name=first_name,last_name=last_name,phone=phone, landline=landline,email=email,address=address, postcode=postcode , created_date=created_date , created_by=created_by  )#first parameter is column name(database) 2nd paarmeter is variable which will take data to database.
        #line 23 data is object for customer class which will call inbuilt function.save and save data to Customer table
        
        data.save()
        
        customer = Customer.objects.get(id=data.id)#first id compares newly created client id from database
        context = {'message':"New client has been created successfuly  ", 'customer_context':customer}
        return render(request, 'New_client_created.html',context)
        # return redirect('/')#/ is deafult page diverts to default home page
    else:
        return render(request, 'add_client_form.html')


# def New_client_created(request):
#     last_client_created = Customer.objects.filter('created_date').last()
#     print(last_client_created)
#     context = {'last_client_created_context':last_client_created}
#     return render(request,'New_client_created.html',context)


def Client_little_info(request):
    find_client = Customer.objects.all()
    context = {'search_clients_context':find_client}
    return render(request, 'Client_little_info.html',context )

def Client_detail_info(request):
    
    return render(request, 'Client_detail_info.html')

    
def search_client(request):
    return render(request,'search_client.html')





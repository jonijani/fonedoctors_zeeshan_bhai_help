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
        data = Customer(first_name=first_name,last_name=last_name,phone=phone, landline=landline,email=email,address=address, postcode=postcode , created_date=created_date   )#first parameter is column name(database) 2nd paarmeter is variable which will take data to database.
        #line 15 data is object for customer class which will call inbuilt function.save and save data to Customer table
        data.save()
        return render(request, 'New_client_created.html',{'message':"New client has been created successfuly  "})
        # return redirect('/')#/ is deafult page diverts to default home page
    else:
        return render(request, 'add_client_form.html')


def New_client_created(request):
    return render(request,'New_client_created.html')

    
def search_client(request):
    return render(request,'search_client.html')





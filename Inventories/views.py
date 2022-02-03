
from django.shortcuts import render, redirect
#from .models import Customer
import datetime
from django.http import HttpResponse

def inventories_dashboard(request):
    return render(request,'inventories_dashboard.html')

def Add_new_part(request):
    return render(request,'Add_new_part.html')




from django.shortcuts import render, redirect
#from .models import Customer
import datetime
from django.http import HttpResponse
from Inventories.models import  *
from Jobs.models import *


def inventories_dashboard(request):
    return render(request,'inventories_dashboard.html')

def Add_new_part(request):
    part = Inventories.objects.all()
    make = Make.objects.all()
    model = Model.objects.all()
    device = Devices.objects.all()
    part_name = Part_name.objects.all()
    colour = Part_colour.objects.all()
    supplier = Supplier.objects.all()

    if request.method == "POST":
        device_name = request.POST.get('device_mobile')
        make_name = request.POST.get('make_name')
        model_name = request.POST.get('model_name')
        part_name = request.POST.get('part_name')
        part_colour = request.POST.get('colour_name')
        supplier_name = request.POST.get('supplier_name')
        quantity_name = request.POST.get('quantity_name')
        cost_name = request.POST.get('cost_name')

        device_v = Devices.objects.get(devices=device_name)
        make_v = Make.objects.get(make=make_name)
        model_v = Model.objects.get(model=model_name)
        part_name_v = Part_name.objects.get(part_name=part_name)
        part_colour_v = Part_colour.objects.get(colour=part_colour)
        supplier_v = Supplier.objects.get(supplier=supplier_name)

        data = Inventories( devices = device_v,
                            make = make_v,
                            model = model_v,
                            part_name = part_name_v,
                            part_colour = part_colour_v,
                            supplier = supplier_v,
                            quantity = quantity_name,
                            cost = cost_name,
                            created_by = request.user,
                            created_date = datetime.datetime.now() 
                            )
        data.save()
        return redirect('part_added',id=data.id)

        

    
    context = {'part_context':part,
                'make_context':make,
                'model_context':model,
                'device_context':device,
                'part_name_context':part_name,
                'colour_context':colour,
                'supplier_context':supplier

                }
    return render(request,'Add_new_part.html',context)

def part_added(request,id):
    part = Inventories.objects.get(id=id)
    context = {'part_context':part}
    return render(request,'part_added.html',context)


def part_detail(request,id):
    part = Inventories.objects.get(id=id)
    context = {'part_detail_context':part}
    return render(request,'part_detail.html',context)







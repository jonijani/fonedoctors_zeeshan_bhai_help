from django.shortcuts import render
from Jobs.models import  *
from .models import *

# def retail_sale_page(request,id):
    
#     return render(request,'retail_sale_page.html')

def retail_sale_page(request,id):
    j_deliver = Jobs.objects.get(id=id)
    
    data = Customer_cart(c_cart=j_deliver)
    data.save()
    
    context = {'j_deliver_context':j_deliver}

    return render(request,'retail_sale_page.html',context)



def customer_cart(request,id):
    cart = Customer_cart.objects.filter(c_cart=id)
    context = {'cart_context':cart}
    return render(request,'customer_cart.html',context)




def daily_sale_report(request,id):
    c_cart = Customer_cart.objects.filter(c_cart=id)
    context = {'c_cart_context':c_cart}
    return render(request,'daily_sale_report.html',context)








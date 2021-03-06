from django.shortcuts import render ,redirect
from Jobs.models import  *
from .models import *

# def retail_sale_page(request,id):
    
#     return render(request,'retail_sale_page.html')

def retail_sale_page(request,id):
    j_deliver = Jobs.objects.get(id=id)

    if request.method == 'POST':
        cost_name = request.POST.get("cost_name")
        data = Customer_cart(c_cart=j_deliver, deliver_cost=cost_name, sale_person=request.user, date=datetime.datetime.now())
        data.save()
        
        customer_cart = Customer_cart.objects.filter(id=data.id).first()
        
        return redirect('customer_cart',customer_cart.id)
    
    context = {'j_deliver_context':j_deliver}

    return render(request,'retail_sale_page.html',context)



def customer_cart(request,id):
    cart = Customer_cart.objects.filter(id=id)
    payment_type = Payment_type.objects.all()
    if request.method == "POST":
        updated_cost_name = request.POST.get("updated_cost_name")
        
        payment_type_name = request.POST.get("payment_type_name")
        delivery_comments_name_v = request.POST.get("delivery_comments_name")

        payment_tpye_v = Payment_type.objects.get(id=payment_type_name)#fetch payment type and id = front end ( whats selecetd from user)
        
        temp = Customer_cart.objects.get(id=id)
         
        # temp.c_cart.job_status= Job_status.objects.get(job_status='Delivered')
        job = temp.c_cart.id# ??
        jobs = Jobs.objects.filter(id=job).update(job_status= Job_status.objects.get(job_status='Delivered'))
        job = temp.c_cart# ??
        f_reciept = Reciepts(reciept=job)
        f_reciept.save()
        cart_save = Customer_cart.objects.filter(id=id).update(payment_type=payment_tpye_v,
                                                            reciept=f_reciept, 
                                                            deliver_cost=updated_cost_name,
                                                            delivery_comments = delivery_comments_name_v,
                                                            
                                                     )
        job_save = Delivered(job_deliver=job, 
                                delivered_on=datetime.datetime.now(),
                                delivered_by=request.user,
                                make_deliver =  temp.c_cart.make,
                                model_deliver =  temp.c_cart.model,
                                fault_deliver =  temp.c_cart.fault,
                                imei_deliver =  temp.c_cart.imei,
                                cost_deliver =  temp.c_cart.cost,
                                delivery_comments = delivery_comments_name_v,
                                delivered=True
                            )
        job_save.save()
        return redirect('reciept',job)

    context = {'cart_context':cart,"payment_type_context": payment_type}
    return render(request,'customer_cart.html',context)




def daily_sale_report(request):
    d_jobs = Customer_cart.objects.all()
    context = {'c_cart_context':c_cart}
    return render(request,'daily_sale_report.html',context)








from django.shortcuts import render
from Jobs.models import  *

def retail_sale_page(request,id):
    j_deliver = Jobs.objects.get(id=id)
    context = {'j_deliver_context':j_deliver}
    return render(request,'retail_sale_page.html',context)









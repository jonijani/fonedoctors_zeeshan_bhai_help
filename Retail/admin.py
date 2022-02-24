from django.contrib import admin

from .models import *

class Customer_cartAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_job_id',  'deliver_cost','get_imei', 'get_make', 'get_model', 'payment_type']

class Daiy_saleAdmin(admin.ModelAdmin):
    list_display = ['id', 'd_sale', 'sale_person']


admin.site.register([Payment_type ])
admin.site.register(Customer_cart,Customer_cartAdmin)
admin.site.register(Daily_sale,Daiy_saleAdmin)

from django.contrib import admin

from .models import *

class Customer_cartAdmin(admin.ModelAdmin):
    list_display = ['id', 'c_cart', 'deliver_cost', 'payment_type']

class Daiy_saleAdmin(admin.ModelAdmin):
    list_display = ['id', 'd_sale', 'sale_person']


admin.site.register([Payment_type ])
admin.site.register(Customer_cart,Customer_cartAdmin)
admin.site.register(Daily_sale,Daiy_saleAdmin)

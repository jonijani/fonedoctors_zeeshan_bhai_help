from django.contrib import admin
from .models import *

class DevicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'devices', 'customer']

class JobsAdmin(admin.ModelAdmin):
    list_display = ['customer','id', 'device', 'make', 'model', 'imei', 'fault', 'payment_status']

admin.site.register([Make,Model,Fault, Accessories, Sale_item, Network, Job_status,Job_update])
admin.site.register(Devices,DevicesAdmin)
admin.site.register(Jobs,JobsAdmin)











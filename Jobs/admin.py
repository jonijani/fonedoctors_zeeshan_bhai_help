from django.contrib import admin
from .models import *

class DevicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'devices', 'customer']

class JobsAdmin(admin.ModelAdmin):
    list_display = ['customer','id', 'device', 'make', 'model', 'imei', 'fault', 'payment_status']

class CompleteAdmin(admin.ModelAdmin):
    list_display = ['c_job', 'complete_update', 'completed_by', 'payment_status_com', 'cost_com', 'completed_on']

admin.site.register([Make,Model,Fault, Accessories, Sale_item, Network, Job_status,Job_update, Fingerprints, Reciepts  ])
admin.site.register(Devices,DevicesAdmin)
admin.site.register(Jobs,JobsAdmin)
admin.site.register(Complete_job,CompleteAdmin)











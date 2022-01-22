from django.contrib import admin
from .models import *

class DevicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'devices', 'customer']

admin.site.register([Make,Model])
admin.site.register(Devices,DevicesAdmin)


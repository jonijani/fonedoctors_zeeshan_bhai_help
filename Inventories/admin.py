from django.contrib import admin
from .models import *

class InventoriesAdmin(admin.ModelAdmin):
    list_display = ['devices','make', 'model', 'part_name', 'part_colour',  'supplier', 'cost']

admin.site.register([Inventory_Devices,Inventory_Make,Inventory_Model, Part_name, Part_colour, Supplier])

admin.site.register(Inventories,InventoriesAdmin)
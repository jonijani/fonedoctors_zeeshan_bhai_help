from django.contrib import admin
from .models import *

class InventoriesAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'devices','make', 'model', 'part_name', 'part_colour',  'supplier', 'cost']

admin.site.register([ Part_name, Part_colour, Supplier])

admin.site.register(Inventories,InventoriesAdmin)







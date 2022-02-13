# from django.db import models
# from Jobs.models import *




# class Part_name(models.Model):
#     part_name = models.CharField(max_length=250)


#     def __str__(self):
#         return self.part_name


# class Part_colour(models.Model):
#     colour = models.CharField(max_length=250)


#     def __str__(self):
#         return self.colour



# class Supplier(models.Model):
#     supplier = models.CharField(max_length=250)


#     def __str__(self):
#         return self.supplier


# class Inventories(models.Model):
#     devices = models.ForeignKey(Devices,on_delete=models.CASCADE, related_name = 'inventory_device')
#     make = models.ForeignKey(Make,on_delete=models.CASCADE, related_name = 'inventory_make')
#     model = models.ForeignKey(Model,on_delete=models.CASCADE, related_name = 'inventory_model')
#     part_name = models.ForeignKey(Part_name,on_delete=models.CASCADE, related_name = 'inventory_part_name')
#     part_colour = models.ForeignKey(Part_colour,on_delete=models.CASCADE, related_name = 'inventory_Part_colour')
#     supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE, related_name = 'inventory_supplier')
#     quantity = models.IntegerField()
#     cost = models.IntegerField()
    


#     def __str__(self):
#         return f"{self.devices.devices} {self.make.make} {self.model.model} {self.part_name} {self.part_colour} {self.quantity} {self.cost}"





from django.urls import path
from .import views

urlpatterns = [
    path('inventories_dashboard/', views.inventories_dashboard, name='inventories_dashboard'),
    path('Add_new_part/', views.Add_new_part, name='Add_new_part'),
    path('part_added/<str:id>', views.part_added, name='part_added'),
    path('part_detail/<str:id>', views.part_detail, name='part_detail')
    

]









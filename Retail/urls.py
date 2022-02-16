from django.urls import path, include
from .import views

urlpatterns = [
    path('retail_sale_page/<str:id>', views.retail_sale_page, name='retail_sale_page'),
    

    

]
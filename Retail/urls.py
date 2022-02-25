from django.urls import path, include
from .import views

urlpatterns = [
    path('retail_sale_page/<str:id>', views.retail_sale_page, name='retail_sale_page'),
    path('customer_cart/<str:id>', views.customer_cart, name='customer_cart'),
    path('daily_sale_report/', views.daily_sale_report, name='daily_sale_report')
    

    

]








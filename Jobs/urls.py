from django.urls import path
from .import views

urlpatterns = [
    path('add_job/', views.add_job, name='add_job'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('search_job/', views.search_job, name='search_job'),
    #path('job_created/', views.job_created, name='job_created'),
    path('add_direct_job/<str:id>', views.add_direct_job, name='add_direct_job'),
    

    

]



















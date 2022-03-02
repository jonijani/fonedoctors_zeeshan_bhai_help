from django.urls import path
from .import views

urlpatterns = [
    path('add_job/', views.add_job, name='add_job'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('search_job/', views.search_job, name='search_job'),
    #path('job_created/<str:id>', views.job_created, name='job_created'),
    path('add_direct_job/<str:id>', views.add_direct_job, name='add_direct_job'),
    path('job_detail_page/<str:id>', views.job_detail_page, name='job_detail_page'),
    path('job_update_page/<str:id>', views.job_update_page, name='job_update_page'),
    path('complete/<str:id>', views.complete, name='complete'),
    path('job_deliver/', views.job_deliver, name='job_deliver'),
    
    path('job_rebook/<str:id>', views.job_rebook, name='job_rebook'),



    #Reciept
    path('reciept/<str:id>', views.reciept, name='reciept'),

    
    #Email
    path('send_email_page/<str:id>/<str:reciept_id>', views.send_email_page, name='send_email_page'),
    path('send_text_page/', views.send_text_page, name='send_text_page'),
    path('contact_by_email/<str:id>/<str:job_id>', views.contact_by_email, name='contact_by_email')
    
    

    

]



















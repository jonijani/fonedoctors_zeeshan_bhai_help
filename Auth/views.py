from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.contrib.auth import login, authenticate, logout

def login_user(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('dashboard')

        
        else:
            return HttpResponse('Invalid username or password')
    # No backend authenticated the credentials
    return render(request,'login.html')
    
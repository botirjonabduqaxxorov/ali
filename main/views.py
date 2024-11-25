from django.shortcuts import render
from . import models
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


@login_required(login_url="login")
def base(request):
    davomat = models.Davomat.objects.all()
    xodim = models.Xodimlar.objects.all()

    context = {
        'davomat': davomat,
        'xodim': xodim,
    }
    return render(request, 'dashboard/base.html', context)

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'dashboard/login/register.html')
        
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        login(request, user)  
        return redirect('home')
    
    return render(request, 'dashboard/login/register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'dashboard/login/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url="login")
def home_view(request):
    return render(request, 'dashboard/login/home.html')
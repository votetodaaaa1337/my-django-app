from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.role == 'admin':
                return redirect('/admin/')
            elif user.role == 'worker':
                return redirect('worker_dashboard')  # создадим позже
            else:
                return redirect('services_list')     # создадим позже
        else:
            return render(request, 'login.html', {'error': 'Неверные данные'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

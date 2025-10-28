from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirige vers /team
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')


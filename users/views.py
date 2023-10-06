from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm

# Create your views here.
def RegisterView(request):
    if request.method == 'POST':
        form= UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can now login!')
            return redirect ('users:login')
    else:
        form= UserRegistrationForm()
    return render(request, 'users/register.html', {'form':form})

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login (request, user)
            return redirect ('blog-home')
    else:
        form = AuthenticationForm()
    
    return render (request, 'users/login.html', {'form':form})

def LogoutView(request):
    logout(request)
    return render(request, 'users/logout.html')

@login_required
def ProfileView(request):
    return render(request, 'users/profile.html')
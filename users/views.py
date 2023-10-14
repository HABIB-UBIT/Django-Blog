from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile

# Create your views here.
def RegisterView(request):
    if request.method == 'POST':
        form= UserRegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            user = form.save()
            profile = Profile(user=user)
            profile.save()
            login(request, user)
            username= form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You can now login!')
            # Create a profile for the user
            # profile = Profile(user=user)
            # profile.save()
            return redirect ('users:login')
            # return redirect('blog:blog-home')
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
    if request.method == 'POST':
        user_form= UserUpdateForm(request.POST, instance=request.user)
        profile_form= ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been Updated.!')
            return redirect ('users:profile')
    else: 
        user_form= UserUpdateForm()
        profile_form= ProfileUpdateForm()
    context={ 
        'user_form':user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/profile.html', context)
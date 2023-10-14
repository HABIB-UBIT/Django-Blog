from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegistrationForm (UserCreationForm):
    email= forms.EmailField()

    class Meta:     # Class meta gives us a nested namespace for configurations and keeps the configurations at one place and within the configuration we're saying that the model will be affected if the user model. the fields that are listed are the fields that we want in the foem and in one order 
        model = User
        fields= ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    email= forms.EmailField()
    class Meta:
        model= User
        fields= ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields= ['image'] 
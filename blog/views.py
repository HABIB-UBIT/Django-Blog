from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
post=[
    {
        'author':'Khalil',
        'title': 'Therefore, I am',
        'content':'Do it your self',
        'date_posted': 'Sep-9,2023'
    }
]
def home(request):
    context={
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
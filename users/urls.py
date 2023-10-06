from django.urls import path
from . import views
app_name= 'users'

urlpatterns=[
    path('register/', views.RegisterView, name='register'),
    path('profile/', views.ProfileView, name='profile'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
]
from django.contrib import admin
from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name = 'jool'
urlpatterns = [
    path("", views.index, name="index"),
    path('login/', auth_views.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
]

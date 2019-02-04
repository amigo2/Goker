from django.urls import path

from . import views


#Paths
urlpatterns = [

    #connected to the function index in  views.py
    path('login', views.login, name='login'),

    #connected to the function register 
    path('register', views.register, name='register'),

    #connected to the method logout
    path('logout', views.logout, name='logout'),

    #connected to the method dashboard single,
    path('dashboard', views.dashboard, name='dashboard'),
]

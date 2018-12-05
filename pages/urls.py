from django.urls import path

from . import views


#Paths
urlpatterns = [

    #connected to the function index in  views.py
    path('', views.index, name='index'),


    #connected to the function about in  views.py
    path('about', views.about, name='about'),
]
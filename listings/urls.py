from django.urls import path

from . import views


#Paths
urlpatterns = [

    #connected to the function index in  views.py
    path('', views.index, name='listings'),

    #connected to the function listing single, pasing a parameter id
    path('<int:listing_id>', views.listing, name='listing'),

    #connected to the method search single, pasing a parameter id
    path('search', views.search, name='search'),
]
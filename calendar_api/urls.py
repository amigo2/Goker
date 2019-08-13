from django.urls import path
from calendar_api import views


#Paths
urlpatterns = [


    #Connect to the Index function in view.py
    path('',views.index, name='calendar'),
]
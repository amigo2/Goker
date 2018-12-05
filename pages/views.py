from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    #connected to the template index.html
    return render(request, 'pages/index.html')


def about(request):
    #connected to the template about.html
    return render(request, 'pages/about.html')
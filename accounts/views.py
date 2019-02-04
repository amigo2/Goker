from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

def register(request):
     # Register User
    if request.method == 'POST':
     first_name = request.POST['first_name']
     last_name  = request.POST['last_name']
     username   = request.POST['username']
     email      = request.POST['email']
     password   = request.POST['password']
     password2   = request.POST['password2']

     if password == password2:
          if User.objects.filter(username=username).exists():
           messages.error(request, 'Ese username esta en uso')
           return redirect('register')
          else:
               if User.objects.filter(email=email).exists():
                    messages.error(request, 'Ese email esta en uso')
                    return redirect('register')
               else:
                    user = User.objects.create_user(username= username, password=password, email=email, first_name=first_name, last_name=last_name)
                    #login after register
                    user.save()
                    messages.success(request, 'YA estas registrado ya puedes logearte')
                    return redirect('index')
                     
     else:
          messages.error(request, 'Los pass no coinciden')
          return redirect('register')
    else:
     return render(request, 'accounts/register.html')

        
def login(request):
    if request.method == 'POST':
          # Login User
          username   = request.POST['username']
          password   = request.POST['password']

          user = auth.authenticate(username=username, password=password)

          if user is not None:
               auth.login(request, user)
               messages.success(request, 'YA estas logeado')
               return redirect('dashboard')
          else:
               messages.error(request,'Credenciales no validas')
               return redirect('login')
    else: 
       return render(request, 'accounts/login.html')


def logout(request):
     if request.method == 'POST':
      auth.logout(request)
      messages.success(request, 'Estas log out')
     return redirect( 'index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')


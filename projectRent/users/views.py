from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from .models import CustomUser

from django.contrib.auth import login, logout, authenticate

# Create your views here.

def test(request):
    return HttpResponse("Test")


def loginUser(request):

    if request.user.is_authenticated:
        return redirect('home-page')
    
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
    
        try:
            CustomUser.objects.get(username=username)
        except:
            messages.error(request, "Username Invalid!!")
        #! Debuging purposes
        print(request.POST['username'])
        print(request.POST['password']) #Safe

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successfully!")
            return redirect('home-page')
        
        else:
            print(user)
            messages.error(request, "Credentials Invalid!!")

    return render(request, 'users/login-page.html')


def logoutUser(request):
    logout(request)
    return redirect('login-page')

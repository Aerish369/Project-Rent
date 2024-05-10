from django.shortcuts import render
from django.http import HttpResponse
from .models import CustomUser

# Create your views here.

def test(request):
    return HttpResponse("Test")


def login(request):
    return render(request, 'users/login-page.html')
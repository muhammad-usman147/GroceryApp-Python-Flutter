from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import User 
# Create your views here.

def UserForm(request):
    X = User.objects.create(name = 'usman shakeel',
    username = 'usman808',
    email = 'ushakeel909@gmail.com',
    password = 'passw')

    return HttpResponse("This is user form page")

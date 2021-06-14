from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def UserForm(request):
    return HttpResponse("This is user form page")

from django.http import response
from django.shortcuts import render

# Create your views here.

def SaveData(request):
    if response.POST.get('save'):
        
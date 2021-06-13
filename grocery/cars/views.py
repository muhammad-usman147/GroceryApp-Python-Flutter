from django.shortcuts import render, HttpResponse
from .models import Car, Driver

def car_details(request, pk):
    x  = Driver.objects.get(pk = pk)
    cars_objs = Car.objects.filter(owner_id = x.id)
    context = {
        'vehicles':cars_objs,
        'drivers':x,
    }
    return render(request, 
    'car_details.html',context)

def secondpage(request):
    return HttpResponse("secondpage")
    
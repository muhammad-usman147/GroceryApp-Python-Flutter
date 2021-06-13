from django.shortcuts import HttpResponse

def firstpage(request):
    return HttpResponse("hello")
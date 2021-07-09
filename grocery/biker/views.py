import json
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Biker_Profile
# Create your views here.

@method_decorator(csrf_exempt, name = 'dispatch')
class BIKER(View):
    #add-biker-info
    #error here
    def post(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            profile = {}
            names = Biker_Profile._meta.fields
            for i in names:
                profile[i.name] = data.get(i.name)
            
            x = Biker_Profile.objects.create(**profile)
            response = {"response":True,
            'msg':'ADDED'}
            return JsonResponse(response)
        except Exception as e:
            response = {"response":False,
            'msg':str(e)}
            return JsonResponse(response)


    '''
    #GET ALL THROUGH DELIVERY STATUS
    def get(self,request,status):
        try:
            data = Biker_Profile.objects.get(delivery_status = status)
            
        except Exception as e:
            pass 
    '''
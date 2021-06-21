from django.shortcuts import render
import json 
from django.http.response import HttpResponse, JsonResponse
from .models import Owner_table
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import  csrf_exempt
# Create your views here.


@method_decorator(csrf_exempt,name = 'dispatch')
class ResponseApiStore(View):
    def put(self,request):
        data = json.loads(request.body.decode('utf-8'))
        names = Owner_table._meta.fields
        create_data = {}
        for i in names:
            create_data[i.name] = data.get(i.name)
        print(create_data)
        X = Owner_table.objects.create(**create_data)
        
        return JsonResponse({"Response": f"{data.get('owner_username')} updated"})

    def get(self,request,entry_point,value):
        try:
            send_data = {}
            #data = json.loads(request.body.decode("utf-8"))
            items = Owner_table.objects.get_or_create(**{entry_point : value})
            names = Owner_table._meta.fields
            Owner_table.objects.getattr
            getattr()
            for i in names:
                send_data[i.name] = items.get(i.name)
            print(send_data)
        except Exception as e:
            print(e)
            
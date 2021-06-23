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
    def post(self,request):
        data = json.loads(request.body.decode('utf-8'))
        names = Owner_table._meta.fields
        create_data = {}
        for i in names:
            create_data[i.name] = data.get(i.name)
        print(create_data)
        X = Owner_table.objects.create(**create_data)
        
        return JsonResponse({"Response": f"{data.get('owner_username')} updated"})

    def get(self,request,value):
        try:
            send_data = []
            items  = Owner_table.objects.filter(owner_username = value)
            
            for item in items:
                send_data.append({
                    "owner_name":item.owner_name,
                    "owner_username":item.owner_username,
                    "owner_email":item.owner_email,
                    "owner_password":item.owner_password,
                    "owner_store_name":item.owner_store_name,
                    "owner_store_type":item.owner_store_type,
                    "owner_store_password":item.owner_store_password,
                })
            return JsonResponse({"DATA":send_data})
        except Exception as e:
            return JsonResponse({"Message":e})
    
    def put(self,request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            us = data['old']['key_username']
            store_owner_data = Owner_table.objects.get(owner_username = us)
            
            
            store_owner_data.owner_name = data['new']['owner_name']
            store_owner_data.owner_username = data['new']['owner_username']
            store_owner_data.ownner_email = data['new']['owner_email']
            store_owner_data.owner_password = data['new']['owner_password']
            store_owner_data.owner_store_name = data['new']['owner_store_name']
            store_owner_data.owner_store_type = data['new']['owner_store_type']
            store_owner_data.owner_store_password = data['new']['owner_store_password']

            store_owner_data.save()
            data = {
                'message_response': f"username {data['old']['username']}  updated to {data['new']['username']}"
            }
            return JsonResponse(data)
        except Exception as e:
            data = {
                'message_ERROR_response': f"{e}"
            }
            return JsonResponse(data)
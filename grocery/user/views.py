from django import views
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
import  json
from django.shortcuts import HttpResponse
from .models import User 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# Create your views here.



#rest api
@method_decorator(csrf_exempt,name = 'dispatch')
class ResponseApiUser(View):

    def post(self,request):
        data = json.loads(request.body.decode("utf-8"))
        name = data.get('name')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        user_data = {
            'name': name,
            'username':username,
            'email':email,
            'password':password
        }
        try:
            _ = User.objects.create(**user_data)
            resp = {
                'message_response':f"{user_data['username']} :: UPDATED"
            }
            return JsonResponse(resp,status = 201)
        except Exception as e:
            resp = {
                'message_response':f"OOPS.. Something went wrong {e}"
            }
            return JsonResponse(resp)

    
    def get(self,request):
        items_count = User.objects.count()
        item_data = User.objects.all()
        datas = []
        for item in item_data:
            datas.append({
                'name':item.name,
                'username':item.username,
                'USER Email':item.email,
                'password':item.password
            })
        '''
        x = {'f':[]}
        names = User._meta.fields
        for i in names:
            x['f'].append(i.name)
        print(x )
        '''
        data = {
            'Total Rows':items_count, 
            'Data View Column':datas,
            
        }

        return JsonResponse(data)


#put and path request for USER data
@method_decorator(csrf_exempt,name = 'dispatch')
class UpdateApiUser(View):
    def patch(self,request,user_id):
        data = json.loads(request.body.decode('utf-8'))
        item = User.objects.get(id = user_id)
        item.username = data['username']
        item.save()
        data = {
            'message_response': f"username {data['username']}  updated"
        }
        return JsonResponse(data)

    
    def put(self,request):
        try:
            
            data = json.loads(request.body.decode('utf-8'))
            us = data['old']['key_username']
            
            user_data = User.objects.get(username = us)
            user_data.name = data['new']['key_name']
            user_data.username = data['new']['key_username']
            user_data.email = data['new']['key_email']
            user_data.password = data['new']['key_password']
            user_data.save()
            message = {
                'message_response': f"{data['old']['key_username']} updated."
            }
            return JsonResponse(message)
        except Exception as e:
            message = {
                'message_ERROR_response': f"{e}"
            }
            return JsonResponse(message)


@method_decorator(csrf_exempt,name = 'dispatch')
class Auth(View):
    #login api
    #user-login-auth
    def get(self,request,username,password):
        try:
            auth = User.objects.filter(username = username,
            password = password)
            if not auth: #if true, means it is empty, no user exists
                return JsonResponse({"msg":False})
            else:
                msg = {}
                for i in auth:
                    msg = {'id' : i.pk,
                        "name":i.name,
                        "username":i.username,
                        
                    }
                return JsonResponse({ "msg" :True,
                "meta_data":msg}
                )
        except Exception  as e:
            return JsonResponse({"error":f"{e}"})        
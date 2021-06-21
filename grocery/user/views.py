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

def UserForm(request):
    X = User.objects.create(name = 'usman shakeel',
    username = 'usman808',
    email = 'ushakeel909@gmail.com',
    password = 'passw')

    return HttpResponse("This is user form page")


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
        data = {
            'Total Rows':items_count, 
            'Data View Column':datas
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt,name = 'dispatch')
class UpdateApiUser(View):
    def patch(self,request,user_id):
        data = json.loads(request.body.decode('utf-8'))
        item = User.objects.get(id = user_id)
        item.username = data['username']
        item.save()
        data = {
            'message_respose': f"username {data['username']}  updated"
        }
        return JsonResponse(data)
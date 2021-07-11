import json
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Biker_Profile, OrderBiker
from cart.models import CartSystem
from user.models import User
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


    
    #GET ALL THROUGH DELIVERY STATUS using delivery condition
    #get-orders-status/
    def get(self,request,status):
        try:
            all_data = OrderBiker.objects.filter(delivery_status = status)
            
            msg = []
            for data in all_data:
                x = CartSystem.objects.get(pk =data.order_id_to_biker_id )
                profile = Biker_Profile.objects.get(pk = data.biker_id_id)
                msg.append({
                    "id":data.pk,
                    'user name': User.objects.get(pk = x.user_id_id).name,
                    'delivery_status':data.delivery_status,
                    'address':data.address,
                    'contact':data.contact,
                    'biker_data':{
                     'order_id':   x.order_id,
                     'name': profile.name,
                     'contact':profile.number
                     
                    }
                })

            information = {"msg":msg}
            return JsonResponse(information)
        except Exception as e:
            return JsonResponse({"msg":str(e)})

    '''
    put function to make the order now-delivering / in-delivering
    from table  cart-system and biker-order

    '''
    def put(request):
        pass
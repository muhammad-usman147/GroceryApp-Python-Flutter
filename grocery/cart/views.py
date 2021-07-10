from json.decoder import JSONDecodeError
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from store.models import Owner_Products
from user.models import User
from .models import CartSystem
from biker.models import Biker_Profile, OrderBiker
from django.views import View
import json
from django.utils.decorators import  method_decorator
from django.views.decorators.csrf import csrf_exempt
import numpy as np
# Create your views here.
@method_decorator(csrf_exempt,name = 'dispatch')
class ADDTOCART(View):
    #add-to-cart/
    def post(self,request):
        try:
            data = json.loads(request.body.decode('utf-8'))

            get_data = CartSystem.objects.all()

            order_id = []
            for i in get_data:
                order_id.append(i.order_id)
            if data.get('order_id') in order_id:
                return JsonResponse({"msg":"order id exists"})
            post_data = {}
            names = CartSystem._meta.fields
            for i in names:
                post_data[i.name] = data.get(i.name)
            post_data["product_id_id"]  = data.get("product_id_id")
            post_data["owner_id_id"]  = data.get("owner_id_id")
            post_data["user_id_id"]  = data.get("user_id_id")
            #print(post_data)
            #subtracting from product table
            product_names = Owner_Products.objects.get(pk = post_data['product_id_id'])



            #product_names = Owner_Products._meta.fields
            print(product_names.item_name)
            print(product_names.quantity)
            print(product_names.price_to_sold)
            print(product_names.Quantity_type)
            print(product_names.owner_id_id)
            if post_data['quantity'] > product_names.quantity:
                return JsonResponse({"error":"Quantity out of range"})
            
            x = CartSystem.objects.create(**post_data)
            return JsonResponse({"msg":"ADDED to CART"})
        except Exception as e:
            return JsonResponse({"msg":f"{e}"})   
    #get-all-to-cart/
    def get(self,request):
        try:
            #data = json.loads(request.body.decode('utf-8'))

            get_data = CartSystem.objects.all()
            send_data = []
            for item in get_data:
                send_data.append({
                    "quantity":item.quantity,
                    "address":item.address,
                    "date":item.date,
                    "payment_method":item.payment_method,
                    "card_payment":item.card_payment,
                    "delivery_status":item.delivery_status,
                    "order_id":item.order_id,
                    "owner_id_id":item.owner_id_id,
                    "product_id_id":item.product_id_id,
                    "user_id_id":item.user_id_id,
                })
            return JsonResponse({"cart_data":send_data})
            
        except Exception as e:
            return JsonResponse({"msg":f"{e}"})  
    #update cart and return the updated cart
    #put-to-cart/
    def put(self,request):
        try:
            item = json.loads(request.body.decode('utf-8'))
            get_filtered_data = CartSystem.objects.get(order_id = item.get("order_id"))
            #---
            #get = CartSystem.objects.get(order_id=item.get("order_id"))
            products_name = Owner_Products.objects.get(pk = item.get("product_id_id"))
            if item.get("quantity") > products_name.quantity:
                return JsonResponse({"error": " Quantity out of range"})

            names = CartSystem._meta.fields
            print([i.name for i in names])
            get_filtered_data.quantity = item.get("quantity")
            get_filtered_data.address=item.get("address")
            get_filtered_data.date=item.get("date")
            get_filtered_data.payment_method=item.get("payment_method")
            get_filtered_data.card_payment=item.get("card_payment")
            get_filtered_data.delivery_status = item.get("delivery_status")
            get_filtered_data.order_id=item.get("order_id")
            get_filtered_data.owner_id_id=item.get("owner_id_id")
            get_filtered_data.product_id_id=item.get("product_id_id")
            get_filtered_data.user_id_id= item.get("user_id_id")
            

            
            send_data = []
            send_data.append({
                    "quantity":item.get("quantity"),
                    "address":item.get("address"),
                    "date":item.get("date"),
                    "payment_method":item.get("payment_method"),
                    "card_payment":item.get("card_payment"),
                    "delivery_status":item.get("delivery_status"),
                    "order_id":item.get("order_id"),
                    "owner_id_id":item.get("owner_id_id"),
                    "product_id_id":item.get("product_id_id"),
                    "user_id_id":item.get("user_id_id"),
                })
            #get_filtered_data.save()
            return JsonResponse({"response":send_data})
                
        except Exception as e:
            return JsonResponse({"response":str(e)})






@method_decorator(csrf_exempt,name = 'dispatch')
class UpdateCartToDGut(View):
    # cart-confirm/
    #confirm cart button
    #subtract from the prodcut
    def post(self,request):
        try:

            data = json.loads(request.body.decode('utf-8'))
            product_id = data.get('product_id')
            
            product_quantity = data.get("quantity")
            item_to_update = Owner_Products.objects.get(pk  = product_id)
            item_to_update.quantity -= product_quantity
            o_id = data.get('order_id')
            cart_item = CartSystem.objects.get(order_id = o_id)
            cart_item.delivery_status = data.get('delivery_status') #should be in-progress
            
            biker = Biker_Profile.objects.values('pk')
            biker_id = [i[0] for i in biker]


            ids = biker_id[np.random.randint(0,len(biker_id))]
            
            
            order = {
                'delivery_status':'in-progress',
                'biker_id_id':ids,
                'order_id_to_biker_id': o_id,
                'address':data.get("address"),
                'contact': data.get("contact")
            }
            _ = OrderBiker.objects.create(**order)
            cart_item.save()
            item_to_update.save()
            print("-"*30,item_to_update.quantity,'-'*30)
            print("-"*30,cart_item.delivery_status,'-'*30)
            return JsonResponse({"response":True,
            'msg':"Cart comfirmed"})
        except Exception as e:
            return JsonResponse({"reponse":False,
            'msg':'Something Went Wrong',
            'error':str(e)})

    #get cart details by id
    def get(self,request,order_id):
        try:
            item = CartSystem.objects.get(order_id,order_id)
  
            send_data = []
            
            #get user email and name
            send_data.append({
                    "quantity":item.quantity,
                    "address":item.address,
                    "date":item.date,
                    "payment_method":item.payment_method,
                    "card_payment":item.card_payment,
                    "delivery_status":item.delivery_status,
                    "order_id":item.order_id,
                    "owner_id_id":item.owner_id_id,
                    "product_id_id":item.product_id_id,
                    "user_id_id":item.user_id_id,
                })
            return JsonResponse({"cart_data":send_data})
            
        except Exception as e:
            return JsonResponse({"response":False,
            'error':str(e)})

        
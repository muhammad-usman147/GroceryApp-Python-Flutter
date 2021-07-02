from json.decoder import JSONDecodeError
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from store.models import Owner_Products
from .models import CartSystem
from django.views import View
import json
from django.utils.decorators import  method_decorator
from django.views.decorators.csrf import csrf_exempt
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
            
            product_names.quantity = product_names.quantity - post_data['quantity']
            product_names.save()
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
            get_filtered_data.save()
            #---
            get = CartSystem.objects.get(order_id=item.get("order_id"))
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
            return JsonResponse({"response":send_data})
                
        except Exception as e:
            return JsonResponse({"response":str(e)})
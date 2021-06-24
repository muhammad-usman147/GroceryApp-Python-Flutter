from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.generic.base import View
from .models import Selling_history
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@method_decorator(csrf_exempt,name = 'dispatch')
class SellingHistory(View):
    def post(self,request):
        try:
            data = json.loads(request.body.decode("utf-8"))
            names = Selling_history._meta.fields
            selling_data = {}
            for i in names:
                print(i.name)
                selling_data[i.name] = data.get(i.name)
            selling_data['owner_product_id_id'] = data.get('owner_product_id_id')
            selling_data['owner_user_id_id'] = data.get('owner_user_id_id')
            x = Selling_history.objects.create(**selling_data)
            return JsonResponse({"RESPONSE":"updated"})
        except Exception as e:
            return JsonResponse({"Response":e})
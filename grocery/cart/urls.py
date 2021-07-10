from django.urls import path  
from .views import ADDTOCART

urlpatterns = [
    path('add-to-cart/',ADDTOCART.as_view()),
    path('get-all-to-cart/',ADDTOCART.as_view()),
    path("put-to-cart/",ADDTOCART.as_view())   
]
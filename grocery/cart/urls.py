from django.urls import path  
from .views import ADDTOCART, UpdateCartToDGut

urlpatterns = [
    path('add-to-cart/',ADDTOCART.as_view()),
    path('get-all-to-cart/',ADDTOCART.as_view()),
    path("put-to-cart/",ADDTOCART.as_view()) ,
    path("cart-confirm/",UpdateCartToDGut.as_view()),
    path('get-user-cart/<str:id>/',UpdateCartToDGut.as_view()),
    path('delete-item-from-cart/',ADDTOCART.as_view())
]
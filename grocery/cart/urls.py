from django.urls import path  
from .views import ADDTOCART, UpdateCartToDGut, Counter

urlpatterns = [
    path('add-to-cart/',ADDTOCART.as_view()),
    path('get-all-to-cart/',ADDTOCART.as_view()),
    path("put-to-cart/",ADDTOCART.as_view()) ,
    path("cart-confirm/",UpdateCartToDGut.as_view()),
    path('get-user-cart/<str:id>/',UpdateCartToDGut.as_view()), #for display items on cart
    path('delete-item-from-cart/',ADDTOCART.as_view()),
    path("get-count-cart/<str:order_id>",Counter.as_view())
]
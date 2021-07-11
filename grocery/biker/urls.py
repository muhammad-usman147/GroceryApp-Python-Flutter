from django.urls import path
from .views import BIKER

urlpatterns = [
    path('add-biker-info/',BIKER.as_view()), #post
    path('get-orders-status/<str:status>',BIKER.as_view()) #get
     
]
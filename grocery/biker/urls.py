from django.urls import path
from .views import BIKER

urlpatterns = [
    path('add-biker-info/',BIKER.as_view()),
    path('get-biker-info/',BIKER.as_view())
    
]
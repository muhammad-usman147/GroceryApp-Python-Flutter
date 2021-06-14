from django.urls import  path
from .views import UserForm

urlpatterns = [
    path('',UserForm,name = 'UserRegistration')
]
from django.urls import  path
from .views import ResponseGetApi, UserForm
from .views import ResponseApiUser

urlpatterns = [
    path('get-user/',ResponseApiUser.as_view()),
    path('get-all-data/',ResponseApiUser.as_view())
]


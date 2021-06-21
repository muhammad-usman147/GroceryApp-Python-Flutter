from django.urls import  path
from .views import  UserForm
from .views import ResponseApiUser, UpdateApiUser

urlpatterns = [
    path('get-user/',ResponseApiUser.as_view()),
    path('get-all-data/',ResponseApiUser.as_view()),
    path('updated_single_data/<int:user_id>',UpdateApiUser.as_view())
]


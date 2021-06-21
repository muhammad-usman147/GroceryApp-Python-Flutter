from django.urls import path
from .views import ResponseApiStore

urlpatterns = [
    path('add-store-data/',ResponseApiStore.as_view()),
    path('get-store-data/<str:entry_point>/<str:value>',ResponseApiStore.as_view()),
]
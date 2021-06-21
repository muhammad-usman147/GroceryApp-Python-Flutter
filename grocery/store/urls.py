from django.urls import path
from .views import ResponseApiStore

urlpatterns = [
    path('get-store-data/',ResponseApiStore.as_view())
]
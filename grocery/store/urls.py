from django.urls import path
from .views import ResponseApiStore, StoreTableApiResponse

urlpatterns = [
    path('add-store-data/',ResponseApiStore.as_view()),
    path('get-store-data/<str:value>',ResponseApiStore.as_view()),
    path('update-store-data/',ResponseApiStore.as_view()),
    path('add-store-item/',StoreTableApiResponse.as_view()),
    path('get-store-item/',StoreTableApiResponse.as_view())
]
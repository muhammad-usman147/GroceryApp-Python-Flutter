from django import urls
from django.urls import path
from django.urls.base import clear_url_caches
from django.urls.resolvers import URLPattern
from django.views.generic.base import View
from .views import SellingHistory

urlpatterns = [
    path("post-history/",SellingHistory.as_view()),
]

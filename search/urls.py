from os import name
from django.urls import URLPattern, path
from.import views


urlpatterns = [
    path('', views.index, name="home"),
    path('search', views.search, name="search")
]
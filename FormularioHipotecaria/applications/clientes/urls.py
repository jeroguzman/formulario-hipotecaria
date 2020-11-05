from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.clientesView.as_view(), name='a-clientes'),
   
]
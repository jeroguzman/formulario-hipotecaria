from django.contrib import admin
from django.urls import path
from . import views

app_name = 'clients_app'

urlpatterns = [
    path('clientes/', views.clientesView.as_view(), name='a-clientes'),
    
]
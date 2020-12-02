from django.contrib import admin
from django.urls import path
from .views import clientesView, ClientDetailView

app_name = 'clients_app'

urlpatterns = [
    path('clientes/', clientesView.as_view(), name='a-clientes'),
    path('cliente/<pk>/', ClientDetailView.as_view(), name='a-cliente'),
]
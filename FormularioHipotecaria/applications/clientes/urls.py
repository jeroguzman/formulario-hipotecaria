from django.contrib import admin
from django.urls import path
from .views import (
    clientesView, 
    ClientDetailView,
    ClientDeleteView
)

app_name = 'clients_app'

urlpatterns = [
    path('clientes/', clientesView.as_view(), name='a-clientes'),
    path('cliente/<pk>/', ClientDetailView.as_view(), name='a-cliente'),
    path('borrarCliente/<pk>/', ClientDeleteView.as_view(), name='a-eliminar-cliente'),
]
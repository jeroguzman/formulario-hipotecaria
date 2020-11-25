from django.urls import path
from .views import (
    BancoView, 
    BancoUpdateView, 
    ActividadView,
    ActividadUpdateView
)

app_name = 'calc_app'

urlpatterns = [
    path('bancos/', BancoView.as_view(), name='c-banks'),
    path('editarBanco/<pk>', BancoUpdateView.as_view(), name='c-edit-banks'),
    path('actividades/', ActividadView.as_view(), name='c-activitys'),
    path('actividades/<pk>', ActividadUpdateView.as_view(), name='c-edit-activity'),
]

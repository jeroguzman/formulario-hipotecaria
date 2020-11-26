from django.urls import path
from .views import (
    BancoView, 
    BancoUpdateView, 
    ActividadView,
    ActividadUpdateView,
    CompanyViews,
    CompanyCreateView,
    CompanyUpdateView,
    CompanyDeleteView
)

app_name = 'calc_app'

urlpatterns = [
    path('bancos/', BancoView.as_view(), name='c-banks'),
    path('editarBanco/<pk>', BancoUpdateView.as_view(), name='c-edit-banks'),
    path('actividades/', ActividadView.as_view(), name='c-activitys'),
    path('actividades/<pk>', ActividadUpdateView.as_view(), name='c-edit-activity'),
    path('empresas/', CompanyViews.as_view(), name='c-empresas'),
    path('crearEmpresa/', CompanyCreateView.as_view(), name='c-crear-empresa'),
    path('editarEmpresa/<pk>', CompanyUpdateView.as_view(), name='c-editar-empresa'),
    path('borrarEmpresa/<pk>', CompanyDeleteView.as_view(), name='c-borrar-empresa'),
]

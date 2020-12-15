from django.urls import path
from .views import (
    UserRegisterView, 
    LoginView, 
    LogoutView,
    promotorListView,
    asesorListView,
    UserDetailView,
    UserUpadateView,
    UserDeleteView,
    UserUpdatePassView,
    CompanyViews,
    CompanyCreateView,
    CompanyUpdateView,
    CompanyDeleteView
)

app_name = 'users_app'

urlpatterns = [
    path('registrarUsuario/', UserRegisterView.as_view(), name='u-register'),
    path('editarUsuario/<pk>/', UserUpadateView.as_view(), name='u-edit'),
    path('usuario/<pk>/', UserDetailView.as_view(), name='u-detail'),
    path('eliminar/<pk>/', UserDeleteView.as_view(), name='u-delete'),
    path('cambiarContraseña/<pk>/', UserUpdatePassView.as_view(), name='u-updatePass'),
    path('login/', LoginView.as_view(), name='u-login'),
    path('logout/', LogoutView.as_view(), name='u-logout'),
    path('promotores/', promotorListView.as_view(), name='u-promotores'),
    path('asesores/', asesorListView.as_view(), name='u-asesores'),
    path('empresas/', CompanyViews.as_view(), name='c-empresas'),
    path('crearEmpresa/', CompanyCreateView.as_view(), name='c-crear-empresa'),
    path('editarEmpresa/<pk>', CompanyUpdateView.as_view(), name='c-editar-empresa'),
    path('borrarEmpresa/<pk>', CompanyDeleteView.as_view(), name='c-borrar-empresa'),
]

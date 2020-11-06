from django.urls import path
from .views import (
    UserRegisterView, 
    LoginView, 
    LogoutView,
    promotorListView,
    asesorListView,
    dashboardListView,
    UserDetailView
    )

app_name = 'users_app'

urlpatterns = [
    path('registrarUsuario/', UserRegisterView.as_view(), name='u-register'),
    path('usuario/<pk>/', UserDetailView.as_view(), name='u-detail'),
    path('login/', LoginView.as_view(), name='u-login'),
    path('logout/', LogoutView.as_view(), name='u-logout'),
    path('promotores/', promotorListView.as_view(), name='u-promotores'),
    path('asesores/', asesorListView.as_view(), name='u-asesores'),
    path('dashboard/', dashboardListView.as_view(), name='u-dashboard'),
]

from django.urls import path
from .views import UserRegisterView

app_name = 'users_app'

urlpatterns = [
    path('registrarUsuario/', UserRegisterView.as_view(), name='u-register'),
]

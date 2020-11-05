from django.urls import path
from .views import UserRegisterView, LoginView

app_name = 'users_app'

urlpatterns = [
    path('registrarUsuario/', UserRegisterView.as_view(), name='u-register'),
    path('login/', LoginView.as_view(), name='u-login'),
]

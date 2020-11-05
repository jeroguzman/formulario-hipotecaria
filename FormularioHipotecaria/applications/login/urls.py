from django.urls import path
from .views import AuthUser

urlpatterns = [
    path('login/', AuthUser.as_view(), name='l-login'),
]
from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.home.urls')),
    re_path('asesores/', include('applications.asesores.urls')),
    re_path('clientes/', include('applications.clientes.urls')),
    re_path('', include('applications.login.urls')),
]

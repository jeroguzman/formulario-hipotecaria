from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view()),
    path("dashboard/", views.dashboardView.as_view(), name='a-dashboard'),
    path("asesores/", views.asesoresView.as_view(), name='a-asesores'),
    path("clientes/", views.clientesView.as_view(), name='a-clientes'),

]
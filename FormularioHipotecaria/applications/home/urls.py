from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view()),
    path("dashboard/", views.dashboardView.as_view()),
    path("asesores/", views.asesoresView.as_view()),
    path("clientes/", views.clientesView.as_view()),

]
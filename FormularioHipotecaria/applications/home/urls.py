from django.contrib import admin
from django.urls import path
from . import views

app_name = 'home_app'

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('dashboard/', views.dashboardView.as_view(), name='a-dashboard'),
    path('pagina_final/', views.FinalView.as_view()),
    path('pagina_final_mejora/', views.FinalViewMejora.as_view()),
]
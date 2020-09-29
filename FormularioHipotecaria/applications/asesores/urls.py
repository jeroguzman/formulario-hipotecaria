from django.urls import path
from .views import  asesorListView, asesorDetailView, asesorCreateView
from . import views

urlpatterns = [

    
    path("asesores/", views.asesorListView.as_view(), name='a-asesores'),
    path('<int:pk>/<slug:slug>/', asesorDetailView.as_view(), name='a-asesor'),
    path("nuevoasesor/", views.asesorCreateView.as_view(), name='a-nuevoasesor'),

]
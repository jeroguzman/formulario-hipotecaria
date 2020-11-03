from django.urls import path
from .views import (
    asesorListView, 
    asesorDetailView, 
    asesorCreateView,
    promotorListView,
    promotorDetailView,
    promotorCreateView,
    dashboardListView
    )
from . import views

urlpatterns = [
    path('asesores/', asesorListView.as_view(), name='a-asesores'),
    path('<int:pk>/<slug:slug>/', asesorDetailView.as_view(), name='a-asesor'),
    path('nuevoAsesor/', asesorCreateView.as_view(), name='a-nuevoasesor'),
    path('promotores/', promotorListView.as_view(), name='a-promotores'),
    path('<int:pk>/<slug:slug>/', promotorDetailView.as_view(), name='a-promotor'),
    path('nuevoPromotor/', promotorCreateView.as_view(), name='a-nuevopromotor'),
    path('dashboard/', dashboardListView.as_view(), name='a-dashboard'),
]
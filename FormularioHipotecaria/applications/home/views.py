from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'

class dashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

class asesoresView(TemplateView):
    template_name = 'dashboard/asesores.html'

class clientesView(TemplateView):
    template_name = 'dashboard/clientes.html'

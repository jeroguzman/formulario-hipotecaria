from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from . import forms


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'

class dashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'
    
class clientesView(TemplateView):
    template_name = 'dashboard/clientes/clientes.html'


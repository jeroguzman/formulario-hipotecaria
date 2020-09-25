from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from . import forms
from . import models

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'

class dashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

class asesoresView(FormView):
    form_class = forms.form_lista_Asesores
    template_name = 'dashboard/asesores.html'


class clientesView(TemplateView):
    template_name = 'dashboard/clientes.html'

class nuevoAsesorView(FormView):
    form_class = forms.form_asesor_alta
    template_name = 'dashboard/nuevoAsesor.html'


class asesorList(ListView):
    model = models.form_lista_Asesores
class asesorDetail(DetailView):
    model = models.form_lista_Asesores

class asesorCreation(CreateView):
    model = models.form_lista_Asesores
    success_url = reverse_lazy('home:a-asesores') 
    fields = ['nombres','email','usuario']
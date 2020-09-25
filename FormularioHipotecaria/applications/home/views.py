from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
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
    fields = ['nombres','email','usuario']
    success_url = reverse_lazy('a-nuevoasesor:a-asesores')
    template_name = 'dashboard/nuevoAsesor.html'


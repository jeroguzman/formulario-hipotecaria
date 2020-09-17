from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from . import forms

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'

class dashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

class asesoresView(FormView):
    form_class = forms.form_asesor_alta
    template_name = 'dashboard/asesores.html'

class clientesView(TemplateView):
    template_name = 'dashboard/clientes.html'

class nuevoAsesorView(FormView):
    form_class = forms.form_asesor_alta
    template_name = 'dashboard/nuevoAsesor.html'


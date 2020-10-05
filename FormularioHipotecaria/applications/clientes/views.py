from django.shortcuts import render
from django.views.generic import TemplateView

class clientesView(TemplateView):
    template_name = 'dashboard/clientes/clientes.html'
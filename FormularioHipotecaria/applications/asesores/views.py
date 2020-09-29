from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import asesores 
from . import forms
from django.views.generic import TemplateView
from django.shortcuts import render

class asesorListView(FormView):
    
    form_class = forms.form_Asesores
    template_name = 'asesores/asesores_list.html'

class asesorDetailView(FormView):
    form_class = forms.form_Asesores
    template_name = 'asesores/asesores_list.html'

class asesorCreateView(CreateView):
    model = asesores
    form_class = asesores
    success_url = reverse_lazy('asesores/nuevoAsesor.html')
    template_name = 'asesores/nuevoAsesor.html'
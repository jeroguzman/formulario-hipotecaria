from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import Asesores, Promotores 
from . import forms
from django.views.generic import TemplateView
from django.shortcuts import render, redirect

# Decoradores

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch (self, request, *args, **kwargs):
        return super(StaffRequiredMixin,self).dispatch(request, *args, **kwargs)


@method_decorator(staff_member_required, name='dispatch')
class asesorListView(ListView):
    model = Asesores
    form_class = forms.form_Asesores
    template_name = 'dashboard/asesores/asesores_list.html'

@method_decorator(staff_member_required, name='dispatch')
class asesorDetailView(DetailView):
    model = Asesores
    form_class = forms.form_Asesores
    template_name = 'dashboard/asesores/asesores_list.html'
    

@method_decorator(staff_member_required, name='dispatch')
class asesorCreateView(CreateView):
    model = Asesores
    fields =   ['nombre', 'usuario', 'email', 'pswd',]
    success_url = reverse_lazy('a-asesores')
    template_name = 'dashboard/asesores/asesores_form.html'

@method_decorator(staff_member_required, name='dispatch')
class promotorListView(ListView):
    model = Promotores
    form_class = forms.form_promotor
    template_name = 'dashboard/asesores/promotores_list.html'

@method_decorator(staff_member_required, name='dispatch')
class promotorDetailView(DetailView):
    model = Promotores
    form_class = forms.form_promotor
    template_name = 'dashboard/asesores/promotores_list.html'

@method_decorator(staff_member_required, name='dispatch')
class promorCreateView(CreateView):
    model = Promotores
    fields = ['nombre', 'usuario', 'email', 'url', 'pswd',]
    success_url = reverse_lazy('a-promotores')
    template_name = 'dashboard/asesores/promotores_form.html'
    
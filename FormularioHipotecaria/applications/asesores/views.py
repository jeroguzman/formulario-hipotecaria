from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import asesores 
from . import forms
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
# Decoradores

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch (self, request, *args, **kwargs):
       # if not request.user.is_staff:
        #    return redirect(reverse_lazy('admin:login'))
        return super(StaffRequiredMixin,self).dispatch(request, *args, **kwargs)



class asesorListView(ListView):
    model = asesores
    form_class = forms.form_Asesores
    template_name = 'dashboard/asesores/asesores_list.html'

class asesorDetailView(DetailView):
    model = asesores
    form_class = forms.form_Asesores
    template_name = 'dashboard/asesores/asesores_list.html'
    

@method_decorator(staff_member_required, name='dispatch')
class asesorCreateView(CreateView):
    model = asesores
    #form_class = forms.form_Asesores
    fields =   ['nombres', 'usuario', 'email', ]
    success_url = reverse_lazy('a-asesores')
    template_name = 'dashboard/asesores/asesores_form.html'
   
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from . import forms
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch (self, request, *args, **kwargs):
        return super(StaffRequiredMixin,self).dispatch(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = 'home/home.html'

@method_decorator(staff_member_required, name="dispatch")
class dashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'

@method_decorator(staff_member_required, name="dispatch")    
class clientesView(TemplateView):
    template_name = 'dashboard/clientes/clientes.html'



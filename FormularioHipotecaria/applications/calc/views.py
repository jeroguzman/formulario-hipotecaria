from django.views.generic import (
    UpdateView, 
    ListView
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Banco, Actividad


# Create your views here.
class BancoView(LoginRequiredMixin, ListView):
    model = Banco
    template_name = 'dashboard/calc/banks.html'
    login_url = reverse_lazy('users_app:u-login')
    paginate_by = 10

    def get_queryset(self):
        queryset = Banco.objects.all()

        return queryset


class BancoUpdateView(LoginRequiredMixin, UpdateView):
    model = Banco
    template_name = 'dashboard/calc/edit_bank.html'
    success_url = reverse_lazy('calc_app:c-banks')
    login_url = reverse_lazy('users_app:login')
    fields = ('factor_millar',)


class ActividadView(LoginRequiredMixin, ListView):
    model = Actividad
    template_name = 'dashboard/calc/actividades.html'
    login_url = reverse_lazy('users_app:u-login')
    paginate_by = 10

    def get_queryset(self):
        queryset = Actividad.objects.all()

        return queryset


class ActividadUpdateView(LoginRequiredMixin, UpdateView):
    model = Actividad
    template_name = 'dashboard/calc/edit_actvidades.html'
    success_url = reverse_lazy('calc_app:c-activitys')
    login_url = reverse_lazy('users_app:login')
    fields = (
        'castigo',
        'endeudamiento',
        )

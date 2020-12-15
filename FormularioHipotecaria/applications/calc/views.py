from django.views.generic import (
    UpdateView, 
    ListView,
    CreateView,
    DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models import Banco, Actividad
from .forms import BancoUpdateForm, ActividadUpdateForm


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
    form_class = BancoUpdateForm
    success_url = reverse_lazy('calc_app:c-banks')
    login_url = reverse_lazy('users_app:login')

    def form_valid(self, form):
        current_user = self.request.user

        if current_user.is_superuser:
            return super(BancoUpdateView, self).form_valid(form)
        else:
            return HttpResponseRedirect(
                reverse('users_app:u-logout')
            )


class ActividadView(LoginRequiredMixin, ListView):
    model = Actividad
    template_name = 'dashboard/calc/actividades.html'
    login_url = reverse_lazy('users_app:u-login')
    paginate_by = 32

    def get_queryset(self):
        queryset = Actividad.objects.all()

        return queryset


class ActividadUpdateView(LoginRequiredMixin, UpdateView):
    model = Actividad
    template_name = 'dashboard/calc/edit_actvidades.html'
    form_class = ActividadUpdateForm
    success_url = reverse_lazy('calc_app:c-banks')
    login_url = reverse_lazy('users_app:login')

    def form_valid(self, form):
        current_user = self.request.user

        if current_user.is_superuser:
            return super(ActividadUpdateView, self).form_valid(form)
        else:
            return HttpResponseRedirect(
                reverse('users_app:u-logout')
            )

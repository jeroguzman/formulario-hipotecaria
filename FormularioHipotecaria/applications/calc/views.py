from django.views.generic import (
    UpdateView, 
    ListView,
    CreateView,
    DeleteView
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Banco, Actividad
from applications.users.models import Company
from .forms import (
    CompanyCreateForm,
    CompanyUpdateForm,
    BancoUpdateForm,
    ActividadUpdateForm
    )


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


class CompanyViews(LoginRequiredMixin, ListView):
    model = Company
    template_name = 'dashboard/calc/empresas.html'
    login_url = reverse_lazy('users_app:u-login')
    paginate_by = 10

    def get_queryset(self):
        queryset = Company.objects.all()

        return queryset


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    template_name = 'dashboard/calc/crear_empresa.html'
    form_class = CompanyCreateForm
    success_url = reverse_lazy('calc_app:c-empresas')
    login_url = reverse_lazy('users_app:u-login')

    def form_valid(self, form):
        empresa = Company.objects.create(
            name=form.cleaned_data['name'],
            logo=form.cleaned_data['logo']
        )
        empresa.save()

        return super(CompanyCreateView, self).form_valid(form)


class CompanyUpdateView(LoginRequiredMixin, UpdateView):
    model = Company
    template_name = 'dashboard/calc/edit_empresa.html'
    form_class = CompanyUpdateForm
    success_url = reverse_lazy('calc_app:c-empresas')
    login_url = reverse_lazy('users_app:login')


class CompanyDeleteView(LoginRequiredMixin, DeleteView):
    model = Company
    template_name = 'dashboard/calc/delete_empresa.html'
    success_url = reverse_lazy('calc_app:c-empresas')
    login_url = reverse_lazy('users_app:u-login')

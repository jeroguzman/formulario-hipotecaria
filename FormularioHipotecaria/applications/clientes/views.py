from django.views.generic import (
    DetailView, 
    ListView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from itertools import chain
from .models import Clientes
from applications.users.models import User


class clientesView(LoginRequiredMixin, ListView):
    model = Clientes
    template_name = 'dashboard/clientes/clientes.html'
    login_url = reverse_lazy('users_app:u-login')
    paginate_by = 20

    def get_queryset(self):
        # Asesores
        if self.request.user.modalidad == 'Asesor':
            if self.request.user.is_superuser: # Administrador
                queryset = Clientes.objects.all()

                return queryset
            else: 
                # Promotores
                queryset_p = User.objects.filter(modalidad='Promotor', asesor=self.request.user.username)
                queryset_c = Clientes.objects.filter(promotor_id=self.request.user.id)

                for promotor in queryset_p:
                    # Clientes
                    queryset = Clientes.objects.filter(promotor_id=promotor.id)
                    queryset_c = list(chain(queryset_c, queryset))

                return queryset_c
        else: # Promotores
            queryset_c = Clientes.objects.filter(promotor_id=self.request.user.id)

            return queryset_c


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Clientes
    template_name = 'dashboard/clientes/cliente_detalle.html'
    login_url = reverse_lazy('users_app:u-login')


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Clientes
    template_name = 'dashboard/clientes/client_delete.html'
    success_url = reverse_lazy('clients_app:a-clientes')
    login_url = reverse_lazy('users_app:u-login')

    def delete(self, *args, **kwargs):
        current_user = self.request.user

        if current_user.is_superuser:
            return super(ClientDeleteView, self).delete(self, *args, **kwargs)
        else:
            return HttpResponseRedirect(
                reverse('users_app:u-logout')
            )

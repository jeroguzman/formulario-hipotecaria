from django.views.generic import DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from itertools import chain
from .models import Clientes
from applications.users.models import User


class clientesView(LoginRequiredMixin, ListView):
    model = Clientes
    template_name = 'dashboard/clientes/clientes.html'
    login_url = reverse_lazy('users_app:u-login')
    paginate_by = 20

    def get_queryset(self):

        if self.request.user.modalidad == 'Asesor':
            # Promotores
            queryset_p = User.objects.filter(modalidad='Promotor', asesor=self.request.user.username)
            queryset_c = Clientes.objects.filter(promotor_id=self.request.user.id)

            for promotor in queryset_p:
                # Clientes
                queryset = Clientes.objects.filter(promotor_id=promotor.id)
                queryset_c = list(chain(queryset_c, queryset))

            return queryset_c
        else:
            queryset_c = Clientes.objects.filter(promotor_id=self.request.user.id)

            return queryset_c


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Clientes
    template_name = 'dashboard/clientes/cliente_detalle.html'
    login_url = reverse_lazy('users_app:u-login')

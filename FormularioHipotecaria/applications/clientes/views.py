from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from applications.clientes.models import Clientes


class clientesView(LoginRequiredMixin, ListView):
    model = Clientes
    template_name = 'dashboard/clientes/clientes.html'
    login_url = reverse_lazy('users_app:u-login')

    def get_queryset(self):
        queryset = Clientes.objects.filter(promotor_id=self.request.user.pk)

        return queryset

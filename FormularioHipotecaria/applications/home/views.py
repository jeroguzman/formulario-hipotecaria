from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from applications.clientes.models import Clientes
from applications.users.models import User



class HomeView(TemplateView):
    template_name = 'home/home.html'

    def post(self, request):

        tramite = request.POST.get('tramite')
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        promotor = request.POST.get('promotor')
        cliente = Clientes.objects.create()
        cliente.nombre = nombre
        cliente.email = correo
        cliente.tramite = tramite
        cliente.telefono = telefono
        cliente.promotor = User.objects.get(id=promotor)
        cliente.save()

        context = {'tramite':tramite, 'nombre':nombre, 'telefono':telefono,
                'correo':correo}
            
        return render(request, self.template_name, context)

class dashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'
    login_url = reverse_lazy('users_app:u-login')


class clientesView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/clientes/clientes.html'
    login_url = reverse_lazy('users_app:u-login')

    



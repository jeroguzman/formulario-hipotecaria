from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect



class HomeView(TemplateView):
    template_name = 'home/home.html'
    
    @csrf_protect
    def index(request):
        print('h')

        tramite = request.POST.get('tramite')
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        submitButton = request.POST.get('submit')

        context = {'tramite':tramite, 'nombre':nombre,
                'correo':correo, 'submitButton':submitButton}
            
        return render(request, 'home/home.html', context)


class dashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/dashboard.html'
    login_url = reverse_lazy('users_app:u-login')


class clientesView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/clientes/clientes.html'
    login_url = reverse_lazy('users_app:u-login')

    



from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.mail import send_mail
from applications.clientes.models import Clientes
from applications.users.models import User


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def post(self, request):
        tramite = request.POST.get('tramite')
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        promotor = User.objects.get(id=request.POST.get('promotor'))

        client = Clientes(
            nombre=nombre,
            email=correo,
            promotor=promotor,
            telefono=telefono,
            tramite=tramite
        )
        client.save()

        client_subject = 'Registro'
        client_message = 'Registro exitoso'
        sender = ''
        send_mail(client_subject, client_message, sender, [correo])

        admin_subject = 'Reigistro de nuevo cliente'
        admin_message = 'Un nuevo cliente se ah registrado bajo el siguiente perfil:'\
            '\n Nombre: {} \n Correo: {} \n Promotor: {} \n Telefono: {} \n Tramite {} '\
            '\n Alcance de credito: {}'.format(
                nombre, 
                correo, 
                promotor, 
                telefono, 
                tramite, 
                client.alcance_credito
                )
        admin_mail = 'admin@mail.com'
        promotor_email = promotor.email
        asesor_email = User.objects.get(username=promotor.asesor).email

        send_mail(admin_subject, admin_message, sender, [admin_mail, promotor_email, asesor_email])

        context = {'tramite':tramite, 'nombre':nombre, 'telefono':telefono,
                'correo':correo}
            
        return render(request, self.template_name, context)

class dashboardView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'dashboard/dashboard.html'
    login_url = reverse_lazy('users_app:u-login')

    def get_queryset(self):
        queryset = User.objects.filter(modalidad='Promotor')

        return queryset

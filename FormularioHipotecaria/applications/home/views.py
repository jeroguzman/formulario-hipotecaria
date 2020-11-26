from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.mail import send_mail
from applications.clientes.models import Clientes
from applications.users.models import User
from applications.calc.calc import get_all_estimates


class HomeView(TemplateView):
    template_name = 'home/home.html'

class dashboardView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'dashboard/dashboard.html'
    login_url = reverse_lazy('users_app:u-login')

    def get_queryset(self):
        queryset = User.objects.filter(modalidad='Promotor', asesor=self.request.user.username)

        return queryset

class FinalView(TemplateView):
    template_name = 'home/pagina_final.html'

    def post(self, request):
        tramite = request.POST.get('tramite')
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        promotor = User.objects.get(id=request.POST.get('promotor'))

        #Mejora
        puntualidad_pagos = request.POST.get('puntualidad_pagos')
        saldo_actual = request.POST.get('saldo_actual')
        pago_mensual = request.POST.get('pago_mensual')
        años_credito = request.POST.get('años_credito')
        tiempo_pagando_años = request.POST.get('tiempo_pagando_años')
        tiempo_pagando_meses = request.POST.get('tiempo_pagando_meses')
        credito_cofinanciado = request.POST.get('credito_cofinanciado')
        institucion_hipotecaria = request.POST.get('institucion_hipotecaria')
        moneda_credito = request.POST.get('moneda_credito')
        pagos_pactados = request.POST.get('pagos_pactados')

        #Compra
        #inmueble_identificado = request.POST.get('inmueble_identificado') #
        valor_inmueble = request.POST.get('valor_inmueble')
        actividad = request.POST.get('actividad')
        institucion = request.POST.get('institucion')
        #pagando_credito_inmb = request.POST.get('pagando_credito_inmb')
        ingreso_mensual = request.POST.get('ingreso_mensual')
        giro_actividad = request.POST.get('giro_actividad')
        estado_civil = request.POST.get('estado_civil')
        #mostrar_mayor_ingreso = request.POST.get('mostrar_mayor_ingreso')
        giro_actividad_co_acreditado = request.POST.get('giro_actividad_co_acreditado')
        actividad_co_acreditado = request.POST.get('actividad_co_acreditado')
        instituciones_co_acreditado = request.POST.get('instituciones_co_acreditado')
        #pagando_credito_inmb_co_acreditado = request.POST.get('pagando_credito_inmb_co_acreditado')
        ingreso_mensual_co_acreditado = request.POST.get('ingreso_mensual_co_acreditado')
        pago_credito = request.POST.get('pago_credito')

        if(actividad == "Empleado" or giro_actividad == "Empleado"):
            giro_actividad = "Asalariado"

        if(actividad_co_acreditado == "Empleado" or giro_actividad_co_acreditado == "Empleado"):
            giro_actividad_co_acreditado = "Asalariado"

        if(giro_actividad == "Independiente"):
            giro_actividad = "Otros"

        if(giro_actividad_co_acreditado == "Independiente"):
            giro_actividad_co_acreditado = "Otros"

        client = Clientes(
            nombre=nombre,
            email=correo,
            promotor=promotor,
            telefono=telefono,
            tramite=tramite,

            #Mejora
            puntualidad_pagos = puntualidad_pagos,
            saldo_actual = saldo_actual,
            pago_mensual = pago_mensual,
            años_credito = años_credito,
            tiempo_pagando_años = tiempo_pagando_años,
            tiempo_pagando_meses = tiempo_pagando_meses,
            credito_cofinanciado = credito_cofinanciado,
            institucion_hipotecaria = institucion_hipotecaria,
            moneda_credito = moneda_credito,
            pagos_pactados = pagos_pactados,

            #Compra
            #inmueble_identificado = inmueble_identificado,
            valor_inmueble = valor_inmueble,
            actividad = actividad,
            institucion = institucion,
            #pagando_credito_inmb = pagando_credito_inmb,
            ingreso_mensual = ingreso_mensual,
            giro_actividad = giro_actividad,
            estado_civil = estado_civil,
            #mostrar_mayor_ingreso = mostrar_mayor_ingreso,
            giro_actividad_co_acreditado = giro_actividad_co_acreditado,
            actividad_co_acreditado = actividad_co_acreditado,
            instituciones_co_acreditado = instituciones_co_acreditado,
            #pagando_credito_inmb_co_acreditado = pagando_credito_inmb_co_acreditado,
            ingreso_mensual_co_acreditado = ingreso_mensual_co_acreditado,
            pago_credito = pago_credito
        )
        client.save()

        msg, alcances = get_all_estimates(client)

        client_subject = 'Registro'
        client_message = 'Registro exitoso\n' + msg
        sender = ''
        send_mail(client_subject, client_message, sender, [correo])

        admin_subject = 'Registro de nuevo cliente'
        admin_message = 'Un nuevo cliente se ha registrado bajo el siguiente perfil:'\
            '\n Nombre: {} \n Correo: {} \n Promotor: {} \n Telefono: {} \n Tramite {} '\
            '\n Alcance de credito: {}\n'.format(
                nombre, 
                correo, 
                promotor, 
                telefono, 
                tramite, 
                client.alcance_credito
                )
        admin_message += msg
        admin_mail = 'correomshipotecaria@gmail.com'
        promotor_email = promotor.email
        asesor_email = User.objects.get(username=promotor.asesor).email

        send_mail(admin_subject, admin_message, sender, [admin_mail, promotor_email, asesor_email])

        context = {'tramite':tramite, 'nombre':nombre, 'telefono':telefono,
                'correo':correo}
            
        return render(request, self.template_name, context)

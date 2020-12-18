from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from itertools import chain
from applications.clientes.models import Clientes
from applications.users.models import User
from applications.calc.calc import get_all_estimates
from .send_emails import Messenger


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        user_id = self.request.GET.get('id')
        user = None

        if user_id is None:
            user = User.objects.get(is_superuser=1)
        else:
            user = User.objects.get(id=user_id)

        user.foto = user.foto.url.replace('staticfiles/', '').replace(' ', '_')
        user.empresa.logo = user.empresa.logo.url.replace('staticfiles/', '').replace(' ', '_')

        ctx['id'] = user.id
        ctx['nombre'] = user.first_name + ' ' + user.last_name
        ctx['foto'] = user.foto.url
        ctx['logo'] = user.empresa.logo.url
        ctx['bienvenida'] = user.bienvenida_txt

        return ctx


class dashboardView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'dashboard/dashboard.html'
    login_url = reverse_lazy('users_app:u-login')

    def get_queryset(self):

        if self.request.user.modalidad == 'Asesor':
            # Promotores
            queryset_p = User.objects.filter(modalidad='Promotor', asesor=self.request.user.username)

            for promotor in queryset_p:
                queryset_c = Clientes.objects.filter(promotor_id=promotor.id)
                queryset_p = list(chain(queryset_p, queryset_c))

            return queryset_p
        else:
            queryset_c = Clientes.objects.filter(promotor_id=self.request.user.id)

            return queryset_c


class FinalView(TemplateView):
    template_name = 'home/pagina_final.html'

    def post(self, request):
        tramite = request.POST.get('tramite')
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        despedida = request.POST.get('despedida')

        try:
            promotor = User.objects.get(id=request.POST.get('promotor'))
        except:
            print('EXCEPT: No se encontro el promotor/asesor en el sistema')
            
            promotor = User.objects.get(is_superuser=1)

        #Compra
        inmueble_identificado = request.POST.get('inmueble_identificado')
        valor_inmueble = request.POST.get('valor_inmueble')
        actividad = request.POST.get('actividad')
        institucion = request.POST.get('institucion')
        pagando_credito_inmb = request.POST.get('pagando_credito_inmb')
        ingreso_mensual = request.POST.get('ingreso_mensual')
        giro_actividad = request.POST.get('giro_actividad')
        estado_civil = request.POST.get('estado_civil')
        co_acreditado = request.POST.get('co_acreditado')
        giro_actividad_co_acreditado = request.POST.get('giro_actividad_co_acreditado')
        actividad_co_acreditado = request.POST.get('actividad_co_acreditado')
        instituciones_co_acreditado = request.POST.get('instituciones_co_acreditado')
        pagando_credito_inmb_co_acreditado = request.POST.get('pagando_credito_inmb_co_acreditado')
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

            #Compra
            inmueble_identificado = inmueble_identificado,
            valor_inmueble = valor_inmueble,
            actividad = actividad,
            institucion = institucion,
            pagando_credito_inmb = pagando_credito_inmb,
            ingreso_mensual = ingreso_mensual,
            giro_actividad = giro_actividad,
            estado_civil = estado_civil,
            co_acreditado = co_acreditado,
            giro_actividad_co_acreditado = giro_actividad_co_acreditado,
            actividad_co_acreditado = actividad_co_acreditado,
            instituciones_co_acreditado = instituciones_co_acreditado,
            pagando_credito_inmb_co_acreditado = pagando_credito_inmb_co_acreditado,
            ingreso_mensual_co_acreditado = ingreso_mensual_co_acreditado,
            pago_credito = pago_credito
        )
        client.save()

        # Obteniendo los alcabces de credito por banco
        alcances, cap_endeudamiento = get_all_estimates(client)

        # Guardando alcances de credito en el modelo cliente
        client.banorte = alcances['BANORTE']
        client.hsbc = alcances['HSBC']
        client.banamex = alcances['BANAMEX']
        client.santander = alcances['SANTANDER']
        client.scotiabanck = alcances['SCOTIABANK']
        client.bx = alcances['BX+']
        client.afirme = alcances['AFIRME']
        client.banregio = alcances['BANREGIO']
        client.save()

        sender = Messenger()
        sender.email_to_admin(client, cap_endeudamiento)
        sender.email_to_client(client)
        # else:
        ## --| Envio de correos en el tramite de Mejora de Hipoteca |-- ##
        #     msg = 'Tramite de mejora de hipoteca'

        context = {'tramite':tramite, 'nombre':nombre, 'telefono':telefono, 'correo':correo, 'despedida':despedida}

        return render(request, self.template_name, context)

class FinalViewMejora(TemplateView):
    template_name = 'home/pagina_final_mejora.html'

    def post(self, request):
        tramite = request.POST.get('tramite')
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        despedida = request.POST.get('despedida')

        try:
            promotor = User.objects.get(id=request.POST.get('promotor'))
        except:
            print('EXCEPT: No se encontro el promotor/asesor en el sistema')
            
            promotor = User.objects.get(is_superuser=1)

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

        )
        client.save()

        context = {'tramite':tramite, 'nombre':nombre, 'telefono':telefono, 'correo':correo, 'despedida':despedida}

        return render(request, self.template_name, context)

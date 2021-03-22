from django.core.mail import send_mail
from django.template import loader
from applications.users.models import User


class Messenger:
    email_admin = 'contacto@mshipotecaria.com'
    email_sender = 'perfiladormultibancario@gmail.com'

    def email_to_admin(self, client, cap_endeudamiento):
        email_prom = client.promotor.email

        admin_subject = 'Perfilador web /{}/{}'.format(client.promotor, client.nombre)
        admin_content = 'Un nuevo cliente se ha registrado en tu enlace de Perfilamiento de Crédito Hipotecario:'
        template_mail = 'admin_mail.html'

        if client.ingreso_mensual_co_acreditado is None:
            client.ingreso_mensual_co_acreditado = 0.0
        
        if client.valor_inmueble is None:
            client.valor_inmueble = 0.0

        tasa_endeudamiento = float(client.pago_credito) / (float(client.ingreso_mensual) + float(client.ingreso_mensual_co_acreditado))
        tasa_endeudamiento = round(tasa_endeudamiento, 2)

        ctx = {
            'asesor': client.promotor.asesor,
            'promotor': client.promotor,
            'nombre_cliente': client.nombre,
            'telefono': client.telefono,
            'correo': client.email,
            'tipo_credito': client.tramite,
            'inmueble_identificado': client.inmueble_identificado,
            'valor_inmueble': '{:,}'.format(float(client.valor_inmueble)),
            'actividad': client.actividad,
            'institucion': client.institucion,
            'pagando_credito_inmb': client.pagando_credito_inmb,
            'ingreso_mensual': '{:,}'.format(float(client.ingreso_mensual)),
            'estado_civil': client.estado_civil,
            'giro_actividad': client.giro_actividad,
            'actividad_co_acreditado': client.actividad_co_acreditado,
            'institucion_co_acreditado': client.instituciones_co_acreditado,
            'pagando_credito_inmb_co_acreditado': client.pagando_credito_inmb_co_acreditado,
            'ingreso_mensual_co_acreditado': '{:,}'.format(float(client.ingreso_mensual_co_acreditado)),
            'suma_ingresos': '{:,}'.format(float(client.ingreso_mensual) + float(client.ingreso_mensual_co_acreditado)),
            'pago_credito': '{:,}'.format(float(client.pago_credito)),
            'tasa_endeudamiento': '{:,}'.format(float(tasa_endeudamiento)),
            'hsbc': client.hsbc,
            'banorte': client.banorte,
            'banamex': client.banamex,
            'santander': client.santander,
            'scotiabank': client.scotiabanck,
            'banregio': client.banregio,
            'afirme': client.afirme,
            'bx': client.bx
        }

        html_mail = loader.render_to_string(template_mail, ctx)
        to_send = []

        try:
            email_as = User.objects.get(username=client.promotor.asesor).email
            to_send = [
                self.email_admin,
                email_prom, 
                email_as
            ]
        except:
            print('EXCEPT: No existe un asesor asignado al usuario ' + str(client.promotor))
            
            to_send = [
                self.email_admin, 
                email_prom
            ]

        send_mail(
            admin_subject, 
            admin_content, 
            self.email_sender, 
            to_send, 
            html_message=html_mail
        )

    def email_to_client(self, client):
        client_subject = 'Perfilador Multibancario'
        client_content = '¡¡Gracias por tu confienza!!'

        if client.promotor.empresa.name == 'Perfilador Multibancario':
            template_mail = 'client_mail_ms.html'
        else:
            template_mail = 'client_mail_other.html'

        ctx = {
            'promotor': client.promotor,
            'promotor_tel': client.promotor.telefono,
            'despedida': client.promotor.despedida_txt,
            'hsbc': client.hsbc,
            'banorte': client.banorte,
            'banamex': client.banamex,
            'santander': client.santander,
            'scotiabank': client.scotiabanck,
            'banregio': client.banregio,
            'afirme': client.afirme,
            'bx': client.bx,
            'empresa': client.promotor.empresa.name
        }
        
        html_mail = loader.render_to_string(template_mail, ctx)

        send_mail(client_subject, client_content, self.email_sender, [client.email], html_message=html_mail)

    def email_to_admin_mejora(self, client):
        email_prom = client.promotor.email

        admin_subject = 'Perfilador web /{}/{}'.format(client.promotor, client.nombre)
        admin_content = 'Un nuevo cliente se ha registrado en tu enlace de Perfilamiento de Crédito Hipotecario:'
        template_mail = 'admin_mail_mejora.html'

        ctx = {
            'asesor': client.promotor.asesor,
            'promotor': client.promotor,
            'nombre_cliente': client.nombre,
            'telefono': client.telefono,
            'correo': client.email,
            'tipo_credito': client.tramite,
            'puntualidad_pagos': client.puntualidad_pagos,
            'saldo_actual': '{:,}'.format(float(client.saldo_actual)),
            'pago_mensual': '{:,}'.format(float(client.pago_mensual)),
            'años_credito': client.años_credito,
            'tiempo_pagando_años': client.tiempo_pagando_años,
            'tiempo_pagando_meses': client.tiempo_pagando_meses,
            'credito_cofinanciado': client.credito_cofinanciado,
            'institucion_hipotecaria': client.institucion_hipotecaria,
            'moneda_credito': client.moneda_credito,
            'pagos_pactados': client.pagos_pactados,

        }

        html_mail = loader.render_to_string(template_mail, ctx)
        to_send = []

        try:
            email_as = User.objects.get(username=client.promotor.asesor).email
            to_send = [
                self.email_admin,
                email_prom, 
                email_as,
            ]
        except:
            print('EXCEPT: No existe un asesor asignado al usuario ' + str(client.promotor))
            
            to_send = [
                self.email_admin, 
                email_prom,
            ]

        send_mail(
            admin_subject, 
            admin_content, 
            self.email_sender, 
            to_send, 
            html_message=html_mail
        )

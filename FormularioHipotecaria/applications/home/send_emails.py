from django.core.mail import send_mail
from django.template import loader
from applications.users.models import User


class Messenger:
    email_admin = 'correomshipotecaria@gmail.com'
    email_sender = 'correomshipotecaria@gmail.com'

    def email_to_admin(self, client, cap_endeudamiento):
        email_prom = client.promotor.email
        email_as = User.objects.get(username=client.promotor.asesor).email
        admin_subject = 'Perfilador web /{}/{}'.format(client.promotor, client.nombre)
        admin_content = 'Un nuevo cliente se ha registrado en tu enlace de Perfilamiento de Crédito Hipotecario:'
        template_mail = 'admin_mail.html'

        if client.ingreso_mensual_co_acreditado is None:
            client.ingreso_mensual_co_acreditado = 0.0

        ctx = {
            'asesor': client.promotor.asesor,
            'promotor': client.promotor,
            'nombre_cliente': client.nombre,
            'telefono': client.telefono,
            'correo': client.email,
            'tipo_credito': client.tramite,
            'inmueble_identificado': client.inmueble_identificado,
            'valor_inmueble': client.valor_inmueble,
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
            'pago_mensual': client.pago_mensual,
            'cap_endeudamiento': '{:,}'.format(cap_endeudamiento)
        }

        html_mail = loader.render_to_string(template_mail, ctx)

        send_mail(
            admin_subject, 
            admin_content, 
            self.email_sender, 
            [self.email_admin, email_prom, email_as], 
            html_message=html_mail
        )

    def email_to_client(self, client):
        client_subject = 'Mi Solución Hipotecaria'
        client_content = '¡¡Gracias por tu confienza!!'

        if client.promotor.modalidad == 'Asesor':
            template_mail = 'client_mail_as.html'
        else:
            template_mail = 'client_mail_prom.html'

        ctx = {
            'despedida': client.promotor.despedida_txt,
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

        send_mail(client_subject, client_content, self.email_sender, [client.email], html_message=html_mail)



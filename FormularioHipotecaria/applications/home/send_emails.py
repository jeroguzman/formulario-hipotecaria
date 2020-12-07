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

        admin_content = ''
        admin_content += 'Un nuevo cliente se ha registrado en tu enlace de Perfilamiento de Crédito Hipotecario:'\
            '\n Asesor: {}\n Promotor: {}\n'\
            '\n Nombre Cliente: {}\n Telefono: {}\n Correo: {}\n'\
            '\n Tipo de Credito: {}\n Inmueble Identificado: {}\n Valor del Inmueble: {}\n'.format(
                client.promotor.asesor,
                client.promotor,
                client.nombre,
                client.telefono,
                client.email,
                client.tramite,
                client.inmueble_identificado,
                client.valor_inmueble
            )

        if client.actividad == 'Empleado':
            admin_content += '\n Actividad: {}\n Cotiza: {}\n Esta pagando crédito Infonavit o Fovissste: {}\n '\
                'Ingreso Mensual: {:,}\n Estado Civil: {}\n'.format(
                client.actividad,
                client.institucion,
                client.pagando_credito_inmb,
                client.ingreso_mensual,
                client.estado_civil
            )
        else:
            admin_content += '\n Actividad: {}\n Ingreso Mensual: {:,}\n Giro: {}\n Estado Civil: {}\n'.format(
                client.actividad,
                client.ingreso_mensual,
                client.giro_actividad,
                client.estado_civil
            )

        admin_content += '\n Actividad Co-Acreditado: {}\n Cotiza: {}\n Esta pagando crédito Infonavit o Fovissste: {}'\
            '\n Ingreso Mensual: {:,}\n'\
            '\n Suma de Ingresos: {:,}\n Compromisos de Pago Mensual: {:,}\n Capacidad de Endeudamiento: {:,}'.format(
                client.actividad_co_acreditado,
                client.instituciones_co_acreditado,
                client.pagando_credito_inmb_co_acreditado,
                float(client.ingreso_mensual_co_acreditado),
                float(client.ingreso_mensual) + float(client.ingreso_mensual_co_acreditado),
                client.pago_mensual,
                cap_endeudamiento
            )

        send_mail(admin_subject, admin_content, self.email_sender, [self.email_admin, email_prom, email_as])

    def email_to_client(self, client):
        client_subject = 'Mi Solución Hipotecaria'
        client_content = 'Gracias por tu confienza!!'
        template_mail = 'client_mail.html'
        ctx = {
            'despedida': client.promotor.despedida_txt,
            'hsbc': client.hsbc,
            'banorte': client.banorte,
            'banamex': client.banamex,
            'santander': client.santander,
            'sacotibank': client.scotiabanck,
            'banregio': client.banregio,
            'afirme': client.afirme,
            'bx': client.bx
        }
        
        html_mail = loader.render_to_string(template_mail, ctx)

        send_mail(client_subject, client_content, self.email_sender, [client.email], html_message=html_mail)



from .models import Banco, Actividad
from applications.clientes.models import Clientes

def get_all_estimates(client=None):
    
    if client is not None:          

        if client.ingreso_mensual_co_acreditado is not None:
            sueldo = float(client.ingreso_mensual) + float(client.ingreso_mensual_co_acreditado)
        else:
            sueldo = float(client.ingreso_mensual)

        actividad = client.giro_actividad
        actividades = Actividad.objects.filter(nombre__startswith=actividad)
        msg = 'Alcances de credito por banco.\n'
        alcances = {}

        for activity in actividades:
            # Cuentas con el ingreso declarado
            ingreso_actividad = float(sueldo) * activity.castigo
            cap_endeudamiento = ingreso_actividad * activity.endeudamiento
            cap_pago = cap_endeudamiento - float(client.pago_credito)

            factor_millar =  Banco.objects.get(id=activity.banco_id).factor_millar
            alcance_credito = round((cap_pago / factor_millar) * 1000, 2)
            banco = Banco.objects.get(id=activity.banco_id).nombre

            alcances[banco] = '${:,}'.format(alcance_credito)
            msg += '{}: ${:,}\n'.format(banco, alcance_credito)

        return msg, alcances


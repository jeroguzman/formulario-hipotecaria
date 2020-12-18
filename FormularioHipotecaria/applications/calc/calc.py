from .models import Banco, Actividad
from applications.clientes.models import Clientes

def get_all_estimates(client=None):
    
    if client is not None:          

        if client.ingreso_mensual_co_acreditado is None:
            client.ingreso_mensual_co_acreditado = 0.0

        sueldo = float(client.ingreso_mensual)
        actividad = client.giro_actividad
        actividades = Actividad.objects.filter(nombre__startswith=actividad)
        sueldo_co_acreditado = float(client.ingreso_mensual_co_acreditado)
        actividad_co_acreditado = client.giro_actividad_co_acreditado
        alcances = {}

        for activity in actividades:
            banco = Banco.objects.get(id=activity.banco_id).nombre
            # Cuentas con el ingreso declarado
            # Acreditado
            ingreso_actividad = sueldo * activity.castigo

            # Co Acreditado
            if client.actividad_co_acreditado is not None:
                co_actividad_str = actividad_co_acreditado + '_' + banco.lower()
                co_actividad = Actividad.objects.get(nombre=co_actividad_str)
                co_ingreso_actividad = sueldo_co_acreditado * co_actividad.castigo
                ingreso_actividad = ingreso_actividad + co_ingreso_actividad

            cap_endeudamiento = ingreso_actividad * activity.endeudamiento
            cap_pago = cap_endeudamiento - float(client.pago_credito)

            factor_millar = Banco.objects.get(id=activity.banco_id).factor_millar
            alcance_credito = round((cap_pago / factor_millar) * 1000, 2)

            alcances[banco] = '${:,}'.format(alcance_credito)

        return alcances, cap_endeudamiento


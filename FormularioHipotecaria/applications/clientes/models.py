from django.db import models
from applications.users.models import User

# Create your models here.
class Clientes(models.Model):
    # datos generales
    nombre = models.CharField(max_length=140)
    email = models.EmailField(max_length=140)
    promotor = models.ForeignKey(User, on_delete=models.PROTECT)
    telefono = models.CharField(max_length=140)
    tramite = models.CharField(max_length=140, blank=True, null=True)
    
    busqueda = models.CharField(max_length=140, blank=True, null=True) # Inicio

    # Mejora Hipoteca
    puntualidad_pagos = models.CharField(max_length=140, blank=True, null=True) 
    saldo_actual = models.FloatField(blank=True, null=True) 
    pago_mensual = models.FloatField(blank=True, null=True) 
    años_credito = models.IntegerField(blank=True, null=True) 
    tiempo_pagando_años = models.CharField(max_length=140, blank=True, null=True) ####
    tiempo_pagando_meses = models.CharField(max_length=140, blank=True, null=True) ####
    credito_cofinanciado = models.CharField(max_length=40, blank=True, null=True)
    institucion_hipotecaria = models.CharField(max_length=140, blank=True, null=True) 
    moneda_credito = models.CharField(max_length=40, blank=True, null=True) 
    pagos_pactados = models.CharField(max_length=40, blank=True, null=True) 

    # Compra
    # inmueble_identificado = models.BooleanField(default=False, blank=True, null=True) #######
    valor_inmueble = models.FloatField(blank=True, null=True) 
    actividad = models.CharField(max_length=140, blank=True, null=True) 
    institucion = models.CharField(max_length=40, blank=True, null=True) 
    # pagando_credito_inmb = models.BooleanField(default=False, blank=True, null=True) ######
    ingreso_mensual = models.FloatField(blank=True, null=True)
    giro_actividad = models.CharField(max_length=40, blank=True, null=True) ##!##
    estado_civil = models.CharField(max_length=40, blank=True, null=True) 
    # mostrar_mayor_ingreso = models.BooleanField(default=False, blank=True, null=True) ####
    giro_actividad_co_acreditado = models.CharField(max_length=40, blank=True, null=True) ##!##
    actividad_co_acreditado = models.CharField(max_length=40, blank=True, null=True) 
    instituciones_co_acreditado = models.CharField(max_length=40, blank=True, null=True) 
    # pagando_credito_inmb_co_acreditado = models.BooleanField(default=False, blank=True, null=True) ####
    ingreso_mensual_co_acreditado = models.FloatField(blank=True, null=True) 
    pago_credito = models.FloatField(blank=True, null=True) 

    # Alcances de credito por banco
    banorte = models.CharField(max_length=40, default='0.0')
    hsbc = models.CharField(max_length=40, default='0.0')
    banamex = models.CharField(max_length=40, default='0.0')
    santander = models.CharField(max_length=40, default='0.0')
    scotiabanck = models.CharField(max_length=40, default='0.0')
    bx = models.CharField(max_length=40, default='0.0')
    afirme = models.CharField(max_length=40, default='0.0')
    banregio = models.CharField(max_length=40, default='0.0')

    # Construcción
    #valor_proyecto = models.FloatField(blank=True, null=True) ### puede ser valor_inmbueble ###

    def __str__(self):
        """Return Clientes name."""
        cliente_str = '{}'.format(self.nombre)

        return cliente_str

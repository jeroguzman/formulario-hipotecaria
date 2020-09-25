from django.db import models

# Create your models here.
class form_lista_Asesores(models.Model):

    # datos generales
    nombres = models.CharField(max_length=140)
    usuario = models.CharField(max_length=140)
    telefono = models.CharField(max_length=140)
    email = models.EmailField(max_length=140)
    nclientes = models.CharField(max_length=140)
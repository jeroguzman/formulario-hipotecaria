from django.db import models

# Create your models here.
class clientes(models.Model):

    # datos generales
    nombres = models.CharField(max_length=140)
    email = models.EmailField(max_length=140)
    telefono = models.CharField(max_length=140)
    promotor = models.CharField(max_length=140)
   
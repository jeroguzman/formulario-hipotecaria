from django.db import models
from applications.asesores.models import Promotores

# Create your models here.
class Clientes(models.Model):
    # datos generales
    nombre = models.CharField(max_length=140)
    email = models.EmailField(max_length=140)
    promotor = models.ForeignKey(Promotores, on_delete=models.PROTECT)
    telefono = models.CharField(max_length=140)

    def __str__(self):
        """Return Clientes name."""
        cliente_str = '{}'.format(self.nombre)

        return cliente_str

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
    alcance_credito = models.FloatField(default=0, blank=True, null=True)

    def __str__(self):
        """Return Clientes name."""
        cliente_str = '{}'.format(self.nombre)

        return cliente_str

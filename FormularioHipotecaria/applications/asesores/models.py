from django.db import models

# Create your models here.
class Asesores(models.Model):
    # datos generales
    nombre = models.CharField(max_length=140)
    usuario = models.CharField(max_length=140)
    email = models.EmailField(max_length=140)
    pswd = models.CharField(max_length=20, default='')

    def __str__(self):
        """Return Asesor name."""
        asesor_str = '{} ({})'.format(
            self.nombre,
            self.usuario
            )

        return asesor_str


class Promotores(models.Model):
    # datos generales
    nombre = models.CharField(max_length=140)
    asesor = models.ForeignKey(Asesores, on_delete=models.PROTECT)
    usuario = models.CharField(max_length=140)
    email = models.EmailField(max_length=140)
    url = models.URLField(max_length=140)
    pswd = models.CharField(max_length=20, default='')

    def __str__(self):
        """Return Promotr name."""
        promotor_str = '{} ({})'.format(
            self.nombre,
            self.usuario
            )

        return promotor_str

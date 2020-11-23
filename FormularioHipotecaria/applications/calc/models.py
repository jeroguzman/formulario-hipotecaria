from django.db import models


# Create your models here.
class Banco(models.Model):
    nombre = models.CharField(max_length=20)
    factor_millar = models.FloatField()

    def __str__(self):
        return self.nombre


class Actividad(models.Model):
    banco = models.ForeignKey(Banco, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=80)
    castigo = models.FloatField()
    endeudamiento = models.FloatField()

    def __str__(self):
        '{} - {}'.format(self.nombre, self.banco)

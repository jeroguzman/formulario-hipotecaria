from django.db import models

# Create your models here.
class asesores(models.Model):
    Puesto =[  
            ("Asesor", "Asesor"), 
            ("Promotor", "Promotor"),  
    ] 

    # datos generales
    nombres = models.CharField(max_length=140)
    usuario = models.CharField(max_length=140)
    puesto = models.CharField(max_length=10, choices=Puesto,)
    email = models.EmailField(max_length=140)
    pswd = models.CharField(max_length=20, default='',)
    
   
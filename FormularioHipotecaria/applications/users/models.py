from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import UserManager
# from django.contrib.auth.hashers import make_password Guardar contraseñas encriptadas

# Create your models here.
class User(AbstractUser, PermissionsMixin):
    MODALIDAD_CHOICES = (
        ('Asesor', 'Asesor'),
        ('Promotor', 'Promotor'),
    )

    # Campos obligatoríos (Asesores)
    first_name = models.CharField(max_length=30, verbose_name='Nombre(s)')
    last_name = models.CharField(max_length=30, verbose_name='Apellidos')
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=13, unique=True)
    modalidad = models.CharField(
        max_length=10, 
        choices=MODALIDAD_CHOICES, 
        default='Promotor'
        )
    asesor = models.CharField(max_length=20, blank=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)
    
    # Campos no obligatoríos (Promotores)
    bienvenida_txt = models.TextField(blank=True)
    despedida_txt = models.TextField(blank=True)
    foto = models.ImageField(
        upload_to='static/img/promotores',
        blank=True
        )
    url = models.URLField(blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'telefono']

    objects = UserManager()

    def get_short_name(self):
        return self.username
        
    def get_full_name(self):
        return '{} {}'.format(self.last_name, self.first_name)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

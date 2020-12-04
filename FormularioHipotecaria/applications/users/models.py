from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import UserManager


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=140)
    logo = models.ImageField(upload_to='static/img/promotores/logos')

    def __str__(self):
        return self.name


class User(AbstractUser, PermissionsMixin):
    MODALIDAD_CHOICES = (
        ('Asesor', 'Asesor'),
        ('Promotor', 'Promotor'),
    )

    # Campos obligatoríos (Asesores)
    first_name = models.CharField(
        max_length=30, 
        verbose_name='Nombre(s)'
        )
    last_name = models.CharField(
        max_length=30, 
        verbose_name='Apellidos'
        )
    username = models.CharField(
        max_length=30, 
        unique=True, 
        verbose_name='Nombre de usuario'
    )
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=13, unique=True)
    modalidad = models.CharField(
        max_length=10, 
        choices=MODALIDAD_CHOICES, 
        default='Asesor'
        )
    empresa = models.ForeignKey(
        Company,
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    asesor = models.CharField(max_length=20, blank=True)

    # Campos no obligatoríos (Promotores)
    bienvenida_txt = models.TextField(blank=True)
    despedida_txt = models.TextField(blank=True)
    foto = models.ImageField(
        upload_to='static/img/promotores', 
        default='static/img/ic-2.png'
        )
    url = models.TextField(blank=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'telefono']
    objects = UserManager()

    def save(self, *args, **kwargs):
        profile_pic = str(self.foto).replace(' ', '_').lower()
        profile_pic = profile_pic.replace('static/', '')

        self.url = 'http://perfilador.mshipotecaria.com/?id={}&first_name={}&last_name={}&profile_pic={}&bienbenida={}&despedida={}'.format(
            self.pk,
            self.first_name,
            self.last_name,
            profile_pic,
            self.bienvenida_txt,
            self.despedida_txt
        )

        super(User, self).save(*args, **kwargs)

    def get_short_name(self):
        return self.username
        
    def get_full_name(self):
        return '{} {}'.format(self.last_name, self.first_name)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

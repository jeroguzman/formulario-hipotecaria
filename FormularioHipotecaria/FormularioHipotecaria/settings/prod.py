from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['138.68.61.212', 'localhost', '127.0.0.1', 'perfilador.mshipotecaria.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'admin_ms',
        'NAME': 'mshprod',
        'PASSWORD': 'msdbadmin',
        'HOST': 'localhost',
        'PORT': '',
        'TEST': {
            'NAME': 'mshprod',
        },
    },
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/


# EMAIL SETTINGS
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'correomshipotecaria@gmail.com' 
EMAIL_HOST_PASSWORD = 'Mshipotecaria20'
EMAIL_PORT = 587

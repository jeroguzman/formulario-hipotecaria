from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager, models.Manager):
    
    def _create_user(self, first_name, last_name, username, email, telefono, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            telefono=telefono,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, first_name, last_name, username, email, telefono, password, **extra_fields):
        return self._create_user(first_name, last_name, username, email, telefono, password, False, False, **extra_fields)

    def create_superuser(self, first_name, last_name, username, email, telefono, password, **extra_fields):
        return self._create_user(first_name, last_name, username, email, telefono, password, True, True, **extra_fields)

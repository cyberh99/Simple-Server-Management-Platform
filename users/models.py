from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()
    rsaKey=models.CharField(max_length=200,null=True)
    gpgKey=models.CharField(max_length=200,null=True)

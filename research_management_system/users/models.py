# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=30, default='user')
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    role = models.CharField(max_length=30, default='user')

    def __str__(self):
        return self.username

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.CharField('E-mail',max_length=150, unique=True)

    #comentar para registrar superusers
    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

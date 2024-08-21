from django.contrib.auth.models import AbstractUser
from django.db import models

class OficialUser(AbstractUser):
    # email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    placa = models.CharField(max_length=10, unique=True)
    id = models.AutoField(primary_key=True)
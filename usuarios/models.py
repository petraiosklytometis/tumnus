from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
  choices_cargo = (('O', 'Operador de Caixa'),
                   ('F', 'Fiscal - Gerente'))
  cargo = models.CharField(max_length=1, choices= choices_cargo)
# Create your models here.

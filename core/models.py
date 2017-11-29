from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class CadastrarObjeto(models.Model):
    nome = models.CharField(max_length=200)
    dono = models.OneToOneField(User, verbose_name= "Dono")
    descricao = models.TextField()

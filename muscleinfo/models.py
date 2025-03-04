from django.db import models
from django.utils import timezone

class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    musculo = models.CharField(max_length=100)
    musculo_residual = models.CharField(max_length=100, default='')
    series = models.IntegerField(default=0)
    carga = models.IntegerField(default=0)
    carga_anterior = models.IntegerField(default=0)
    repeticoes = models.IntegerField(default=0)
    repeticoes_anterior = models.IntegerField(default=0)
    infos = models.TextField()
    data = models.DateField(default=timezone.now)
    data_anterior = models.DateField(blank=True, null=True)
    user_id = models.IntegerField(default=0)
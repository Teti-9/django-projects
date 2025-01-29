from django.db import models

class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    musculo = models.CharField(max_length=100)
    musculo_residual = models.CharField(max_length=100, default='')
    series = models.IntegerField(default=0)
    infos = models.TextField()
    user_id = models.IntegerField(default=0)
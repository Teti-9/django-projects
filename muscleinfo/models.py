from django.db import models
from django.utils import timezone

class ProcurarManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
class Exercicio(models.Model):
    nome = models.CharField(
        max_length=100,
        help_text='Nome do exercício.',
        verbose_name='Nome do exercício'
        )
    
    musculo = models.CharField(
        max_length=100,
        help_text='Músculo.',
        verbose_name='Músculo'
        )

    musculo_residual = models.CharField(
        max_length=100, 
        default='',
        help_text='Músculo residual.',
        verbose_name='Músculo residual'
        )

    series = models.IntegerField(
        default=0,
        help_text='Número de séries.',
        verbose_name='Número de séries'
        )

    carga = models.IntegerField(
        default=0,
        help_text='Carga utilizada.',
        verbose_name='Carga utilizada'
        )

    carga_anterior = models.IntegerField(
        default=0,
        help_text='Carga utilizada anteriormente.',
        verbose_name='Carga utilizada anteriormente'
        )

    repeticoes = models.IntegerField(
        default=0,
        help_text='Número de repetições.',
        verbose_name='Número de repetições'
        )

    repeticoes_anterior = models.IntegerField(
        default=0,
        help_text='Número de repetições anterior.',
        verbose_name='Número de repetições anterior'
        )

    infos = models.TextField()

    data = models.DateTimeField(
        default=timezone.now,
        help_text='Data do exercício.',
        verbose_name='Data do exercício'
        )

    data_anterior = models.DateTimeField(
        blank=True, 
        null=True,
        help_text='Data do exercício anterior.',
        verbose_name='Data do exercício anterior'
        )

    user_id = models.IntegerField(
        default=0,
        help_text='ID do usuário.',
        verbose_name='ID do usuário'
        )

    objects = models.Manager()
    procurar = ProcurarManager()

    def __str__(self):
        return f"{self.nome} - {self.musculo}"

    class Meta:
        verbose_name_plural = "Exercícios"
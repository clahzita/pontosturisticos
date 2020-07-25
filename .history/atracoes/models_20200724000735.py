from django.db import models
from atracoes.models import Atracao

class Atracao(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    horario_func = models.TextField()
    idade_minima = models.IntegerField()
    atracoes = models.ManyToManyField(Atracao)
    def __str__(self):
        return self.nome
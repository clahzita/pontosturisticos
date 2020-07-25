from django.db import models

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
from django.db import models
from django.contrib.auth.models import User

class Comentario(models.Model):
    usuario = models.ForeignKey(User)
    cometario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=True)
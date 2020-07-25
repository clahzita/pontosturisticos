from django.db import models

class Comentario(models.Model):
    usuario = models.ForeignKey(User)
    cometario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
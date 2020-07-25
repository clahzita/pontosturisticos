from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=True)
    nota = models.DecimalField(max_digits=3, decimal_places=2, validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ])
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username + " - " + self.data.strftime('%Y-%m-%d %H:%M')
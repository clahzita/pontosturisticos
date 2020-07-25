from django.db import models
from django.contrib.auth.models import User

class Avaliacao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
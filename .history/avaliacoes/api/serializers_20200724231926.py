from rest_framework import serializers
from avaliacoes.models import Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ('id','usuario','comentario','data','aprovado')
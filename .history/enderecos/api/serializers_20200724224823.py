from rest_framework import serializers
from enderecos.models import Endereco

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id','nome','descricao','horario_func','idade_minima']
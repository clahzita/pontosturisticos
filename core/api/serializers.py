from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from atracoes.api.serializers import AtracaoSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from comentarios.api.serializers import ComentarioSerializer
from core.models import PontoTuristico
from enderecos.api.serializers import EnderecoSerializer



class CompletoPontoTuristicoSerializer(serializers.ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    comentarios = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)

    class Meta:
        model = PontoTuristico
        fields = ['id','nome','descricao','aprovado','foto','atracoes','endereco','comentarios','avaliacoes']

class PontoTuristicoSerializer(serializers.ModelSerializer):
    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ['id','nome','descricao','aprovado','foto','atracoes','endereco',
                  'comentarios','avaliacoes', 'descricao_completa', 'descricao_completa2']

    def get_descricao_completa(self, obj):
        return "%s - %s" % (obj.nome, obj.descricao)
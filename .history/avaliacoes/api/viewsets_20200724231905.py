from rest_framework import viewsets
from .serializers import AvaliacaoSerializer
from avaliacoes.models import Avaliacao
class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer
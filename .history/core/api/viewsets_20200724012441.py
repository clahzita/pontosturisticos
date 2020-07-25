from rest_framework import viewsets
from core.models import PontoTuristico

class PontoTuristicoViewSet(ModelViewSet):
    query_set = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer


from rest_framework.viewsets import ModelViewSet
from .models import PontoTuristico

class PontoTuristicoViewSet(ModelViewSet):
    query_set = PontoTuristico.objects.all()


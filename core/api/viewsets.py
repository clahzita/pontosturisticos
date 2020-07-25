from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    serializer_class = PontoTuristicoSerializer
    def get_queryset(self):
        return PontoTuristico.objects.filter(aprovado=True)

    def list(self, request, *args, **kwargs):
        PontoTuristico.objects.filter(aprovado=True)
        return super(PontoTuristicoViewSet,self).list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet,self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet,self).destroy(request, *args, **kwargs)

    #get one
    def retrieve(self, request, *args, **kwargs):
        return super(PontoTuristicoViewSet,self).retrieve(request, *args, **kwargs)

    @action(methods=['get'], detail=True)
    def denunciar(self, request, pk=None):
        return Response({"denunciar": "eita!"})


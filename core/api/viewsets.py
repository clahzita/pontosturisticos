from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(viewsets.ModelViewSet):
    serializer_class = PontoTuristicoSerializer

    permission_classes = [IsAdminUser]
    authentication_classes = (TokenAuthentication,)

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nome','descricao','endereco__linha1']
    #ordering_fields = ['nome']
    #ordering = ['nome'] default é por pk
    #lookup_field = 'nome' precisa um campo exclusivo, é a identificação do objeto, geralmente é o pk

    def get_queryset(self):
        id = self.request.query_params.get('id',None)
        nome = self.request.query_params.get('nome', None)
        descricao = self.request.query_params.get('descricao', None)

        #lazyload: nao vai no banco realmente, nao se preocupar sobre performance
        queryset = PontoTuristico.objects.all()

        if id:
            queryset = queryset.filter(pk=id)

        if nome:
            queryset = queryset.filter(nome__iexact=nome)

        if descricao:
            queryset = queryset.filter(descricao__iexact=descricao)

        return queryset

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

    @action(methods=['get'], detail=False)
    def completo(self, request, pk=None):
        return Response({"denunciar": "eita!"})

    @action(methods=['post'], detail=True)
    def associa_atracoes(self, request, id=None):
        atracoes = request.data['ids']

        ponto = PontoTuristico.objects.get(id=id)

        ponto.atracoes.set(atracoes)

        ponto.save()

        return Response({ponto.atracoes})

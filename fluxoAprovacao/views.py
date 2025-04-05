from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from fluxoAprovacao.models import FluxoAprovacao, EtapaFluxo, Etapa
from fluxoAprovacao.serializer import FluxoAprovacaoSerializer, EtapaFluxoSerializer, EtapaSerializer
from rest_framework.authentication import BasicAuthentication

# Create your views here.

class FluxoAprovacaoViewSet(viewsets.ModelViewSet):
    """ ViewSet para o modelo FluxoAprovacao """
    queryset = FluxoAprovacao.objects.all()
    serializer_class = FluxoAprovacaoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return FluxoAprovacao.objects.all()

class EtapaViewSet(viewsets.ModelViewSet):
    """ ViewSet para o modelo Etapa """
    queryset = Etapa.objects.all()
    serializer_class = EtapaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Etapa.objects.all()

class EtapaFluxoViewSet(viewsets.ModelViewSet):
    """ ViewSet para o modelo EtapaFluxo """
    queryset = EtapaFluxo.objects.all()
    serializer_class = EtapaFluxoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return EtapaFluxo.objects.all()

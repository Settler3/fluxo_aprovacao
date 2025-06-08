from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from solicitacao.models import Solicitacao, HistoricoSolicitacao, AnexoSolicitacao
from solicitacao.serializer import SolicitacaoSerializer, HistoricoSolicitacaoSerializer, AnexoSolicitacaoSerializer
from rest_framework.authentication import BasicAuthentication, TokenAuthentication

class SolicitacaoViewSet(viewsets.ModelViewSet):
    """ ViewSet para o modelo Solicitacao """
    queryset = Solicitacao.objects.all()
    serializer_class = SolicitacaoSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Solicitacao.objects.all()

class HistoricoSolicitacaoViewSet(viewsets.ModelViewSet):
    """ ViewSet para o modelo HistoricoSolicitacao """
    queryset = HistoricoSolicitacao.objects.all()
    serializer_class = HistoricoSolicitacaoSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HistoricoSolicitacao.objects.all()

class AnexoSolicitacaoViewSet(viewsets.ModelViewSet):
    """ ViewSet para o modelo AnexoSolicitacao """
    queryset = AnexoSolicitacao.objects.all()
    serializer_class = AnexoSolicitacaoSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return AnexoSolicitacao.objects.all()

# Create your views here.


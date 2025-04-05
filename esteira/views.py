from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from esteira.models import Esteira, EsteiraFluxo
from esteira.serializer import EsteiraSerializer, EsteiraFluxoSerializer
from rest_framework.authentication import BasicAuthentication

# Create your views here.
class EsteiraViewSet(viewsets.ModelViewSet):
    """ ViewSet para o modelo Esteira """
    queryset = Esteira.objects.all()
    serializer_class = EsteiraSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Esteira.objects.all()

class EsteiraFluxoViewSet(viewsets.ModelViewSet):
    """ ViewSet para o modelo EsteiraFluxo """
    queryset = EsteiraFluxo.objects.all()
    serializer_class = EsteiraFluxoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return EsteiraFluxo.objects.all()

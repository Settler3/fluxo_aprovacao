from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from usuario.models import Usuario, Grupo, Permissao
from usuario.serializer import UsuarioSerializer, GrupoSerializer, PermissaoSerializer
from rest_framework.authentication import BasicAuthentication, TokenAuthentication

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    """ ViewSet para o modelo Usuario """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class GrupoViewSet(viewsets.ModelViewSet):
    """ ViewSet para o modelo Grupo """
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class PermissaoViewSet(viewsets.ModelViewSet):
    """ ViewSet para o modelo Permissao """
    queryset = Permissao.objects.all()
    serializer_class = PermissaoSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
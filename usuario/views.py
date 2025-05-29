from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from usuario.models import Usuario, Grupo, Permissao, GrupoPermissao, UsuarioGrupo
from usuario.serializer import UsuarioSerializer, GrupoSerializer, PermissaoSerializer, GrupoPermissaoSerializer, UsuarioGrupoSerializer
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

class GrupoPermissaoViewSet(viewsets.ModelViewSet):
    """ ViewSet para o modelo GrupoPermissao """
    queryset = GrupoPermissao.objects.all()
    serializer_class = GrupoPermissaoSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class UsuarioGrupoViewSet(viewsets.ModelViewSet):
    """ ViewSet para o modelo UsuarioGrupo """
    queryset = UsuarioGrupo.objects.all()
    serializer_class = UsuarioGrupoSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class GrupoPermissaoListView(generics.ListAPIView):
    """ View para listar as permissões de um grupo """
    serializer_class = GrupoPermissaoSerializer
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        grupo_id = self.kwargs['id']
        return GrupoPermissao.objects.filter(grupo_id=grupo_id)
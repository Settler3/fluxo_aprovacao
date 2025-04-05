from django.urls import path, include
from usuario.views import UsuarioViewSet, GrupoViewSet, PermissaoViewSet, GrupoPermissaoViewSet, UsuarioGrupoViewSet, GrupoPermissaoListView, UsuarioGrupoListView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuario', UsuarioViewSet, basename='Usuarios')
router.register('grupo', GrupoViewSet, basename='Grupos')
router.register('permissao', PermissaoViewSet, basename='Permissoes')
router.register('grupo-permissao', GrupoPermissaoViewSet, basename='GrupoPermissao')
router.register('usuario-grupo', UsuarioGrupoViewSet, basename='UsuarioGrupo')

urlpatterns = [
    path('', include(router.urls)),
    path('grupo/<int:id>/permissoes/', GrupoPermissaoListView.as_view()),
    path('usuario/grupos', UsuarioGrupoListView.as_view()),
]
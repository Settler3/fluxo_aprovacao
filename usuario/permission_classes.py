from rest_framework.permissions import BasePermission

class PodeCriarSolicitacao(BasePermission):
    """
    Permissão para criar solicitações.
    Somente usuários autenticados podem criar solicitações.
    """
    def has_permission(self, request, view):
        return True
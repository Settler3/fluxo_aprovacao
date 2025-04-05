from django.urls import path, include
from fluxoAprovacao.views import FluxoAprovacaoViewSet, EtapaViewSet, EtapaFluxoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('fluxo-aprovacao', FluxoAprovacaoViewSet, basename='FluxosAprovacao')
router.register('etapa', EtapaViewSet, basename='Etapas')
router.register('etapa-fluxo', EtapaFluxoViewSet, basename='EtapasFluxo')

urlpatterns = [
    path('', include(router.urls)),
]
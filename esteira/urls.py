from django.urls import path, include
from esteira.views import (
    EsteiraViewSet,
    EsteiraFluxoViewSet,
)
from rest_framework import routers

router = routers.DefaultRouter()
router.register('esteira', EsteiraViewSet, basename='Esteira')
router.register('fluxo-esteira', EsteiraFluxoViewSet, basename='FluxoEsteira')

urlpatterns = [
    path('', include(router.urls)),
]
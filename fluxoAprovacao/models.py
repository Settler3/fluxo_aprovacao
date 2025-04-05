from django.db import models

# Create your models here.

class FluxoAprovacao(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Fluxo de Aprovação'
        verbose_name_plural = 'Fluxos de Aprovação'
        ordering = ['nome']

class Etapa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Etapa'
        verbose_name_plural = 'Etapas'
        ordering = ['nome']

class EtapaFluxo(models.Model):
    id = models.AutoField(primary_key=True)
    fluxo_aprovacao = models.ForeignKey(FluxoAprovacao, on_delete=models.CASCADE, related_name='etapas')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE, related_name='fluxos_aprovacao')
    etapa_anterior = models.ForeignKey(Etapa, null=True, blank=True, on_delete=models.SET_NULL, related_name='etapas_sequentes')

    def __str__(self):
        return f"{self.fluxo_aprovacao.nome} - {self.etapa.nome}"

    class Meta:
        verbose_name = 'Etapa do Fluxo de Aprovação'
        verbose_name_plural = 'Etapas do Fluxo de Aprovação'
        ordering = ['etapa']
        indexes = [
            models.Index(fields=['fluxo_aprovacao', 'etapa', 'etapa_anterior'], name='fluxo_etapa_index'),
        ]
        constraints = [
            models.UniqueConstraint(fields=['fluxo_aprovacao', 'etapa', 'etapa_anterior'], name='unique_fluxo_etapa')
        ]
from django.db import models
# Create your models here.

class Esteira(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Esteira'
        verbose_name_plural = 'Esteiras'
        ordering = ['nome']

class EsteiraFluxo(models.Model):
    id = models.AutoField(primary_key=True)
    esteira = models.OneToOneField(Esteira, on_delete=models.CASCADE, related_name='fluxos')
    fluxo_aprovacao = models.ForeignKey('fluxoAprovacao.FluxoAprovacao', on_delete=models.CASCADE, related_name='esteira')

    def __str__(self):
        return f"{self.esteira.nome} - {self.fluxo_aprovacao.nome}"

    class Meta:
        verbose_name = 'Esteira do Fluxo de Aprovação'
        verbose_name_plural = 'Esteiras do Fluxo de Aprovação'
        indexes = [
            models.Index(fields=['esteira', 'fluxo_aprovacao']),
        ]
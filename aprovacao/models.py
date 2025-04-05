from django.db import models
from usuario.models import Usuario
from esteira.models import Esteira
from fluxoAprovacao.models import Etapa

# Create your models here.

class Aprovacao(models.Model):
    id = models.AutoField(primary_key=True)
    comentario = models.TextField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='aprovacoes')
    data_aprovacao = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[
        ('Pendente', 'Pendente'),
        ('Aprovado', 'Aprovado'),
        ('Rejeitado', 'Rejeitado')
    ], default='Pendente')
    data_modificacao = models.DateTimeField(auto_now=True)
    esteira = models.ForeignKey(Esteira, on_delete=models.CASCADE, related_name='aprovacoes')
    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE, related_name='aprovacoes')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Aprovação'
        verbose_name_plural = 'Aprovações'

class HistoricoAprovacao(models.Model):
    id = models.AutoField(primary_key=True)
    aprovacao = models.ForeignKey(Aprovacao, on_delete=models.CASCADE, related_name='historicos')
    data_historico = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='historicos')

    def __str__(self):
        return f"{self.aprovacao.nome} - {self.status}"

    class Meta:
        verbose_name = 'Histórico de Aprovação'
        verbose_name_plural = 'Históricos de Aprovação'
        ordering = ['data_historico']
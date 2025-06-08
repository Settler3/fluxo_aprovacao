from django.db import models

# Create your models here.

class Solicitacao(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    esteira = models.ForeignKey('esteira.Esteira', on_delete=models.CASCADE, related_name='solicitacoes')

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = 'Solicitação'
        verbose_name_plural = 'Solicitações'
        ordering = ['data_criacao']
        indexes = [
            models.Index(fields=['usuario', 'esteira']),
        ]
        permissions = [
            ('pode_criar_solicitacao', 'Pode criar solicitações'),
            ('pode_editar_solicitacao', 'Pode editar solicitações'),
            ('pode_deletar_solicitacao', 'Pode deletar solicitações'),
            ('pode_visualizar_solicitacao', 'Pode visualizar solicitações'),
            ('pode_adicionar_anexo_solicitacao', 'Pode adicionar anexos a solicitações'),
            ('pode_visualizar_historico_solicitacao', 'Pode visualizar histórico de solicitações'),
            ('pode_adicionar_historico_solicitacao', 'Pode adicionar histórico a solicitações'),
            ('pode_visualizar_anexo_solicitacao', 'Pode visualizar anexos de solicitações'),
            ('pode_deletar_anexo_solicitacao', 'Pode deletar anexos de solicitações'),
            ('pode_editar_anexo_solicitacao', 'Pode editar anexos de solicitações'),
            ('pode_visualizar_solicitacoes_usuario', 'Pode visualizar solicitações de outros usuários'),
            ('pode_visualizar_solicitacoes_esteira', 'Pode visualizar solicitações de uma esteira específica'),
        ]

class HistoricoSolicitacao(models.Model):
    id = models.AutoField(primary_key=True)
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE, related_name='historicos')
    data_historico = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='historicos_solicitacoes')

    def __str__(self):
        return f"{self.solicitacao.titulo} - {self.status}"
    
    class Meta:
        verbose_name = 'Histórico de Solicitação'
        verbose_name_plural = 'Históricos de Solicitações'
        ordering = ['data_historico']
        indexes = [
            models.Index(fields=['solicitacao', 'usuario']),
        ]

class AnexoSolicitacao(models.Model):
    id = models.AutoField(primary_key=True)
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE, related_name='anexos')
    arquivo = models.FileField(upload_to='anexos/')
    data_upload = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='anexos_solicitacoes')

    def __str__(self):
        return f"Anexo de {self.solicitacao.titulo} - {self.arquivo.name}"

    class Meta:
        verbose_name = 'Anexo de Solicitação'
        verbose_name_plural = 'Anexos de Solicitações'
        ordering = ['data_upload']
        indexes = [
            models.Index(fields=['solicitacao', 'usuario']),
        ]
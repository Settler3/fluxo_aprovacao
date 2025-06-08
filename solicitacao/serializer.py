from rest_framework import serializers
from solicitacao.models import Solicitacao, AnexoSolicitacao, HistoricoSolicitacao

class SolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitacao
        fields = ['id', 'titulo', 'descricao', 'data_criacao', 'usuario', 'esteira', 'grupo']
        extra_kwargs = {
            'usuario': {'required': True, 'write_only': True},
            'esteira': {'required': True, 'write_only': True},
            'grupo': {'required': True, 'write_only': True}
        }

    def validate_titulo(self, value):
        if Solicitacao.objects.filter(titulo=value).exists():
            raise serializers.ValidationError("Este título de solicitação já está em uso.")
        return value
    
    def validate(self, attrs):
        if not attrs.get('titulo'):
            raise serializers.ValidationError("O título é obrigatório.")
        
        if not attrs.get('descricao'):
            raise serializers.ValidationError("A descrição é obrigatória.")
        return attrs
    
class AnexoSolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnexoSolicitacao
        fields = ['id', 'solicitacao', 'arquivo', 'data_upload', 'usuario']
        extra_kwargs = {
            'solicitacao': {'required': True, 'write_only': True},
            'usuario': {'required': True, 'write_only': True}
        }

    def validate_arquivo(self, value):
        if not value.name.endswith(('.pdf', '.xls', '.xlsx', '.doc', '.docx', '.txt', '.csv', '.ppt', '.pptx', '.zip', '.rar')):
            raise serializers.ValidationError("O arquivo deve ser um PDF, Excel, Word, Texto, CSV, PowerPoint ou arquivo compactado.")
        return value
    
class HistoricoSolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoSolicitacao
        fields = ['id', 'solicitacao', 'data_historico', 'status', 'usuario']
        extra_kwargs = {
            'solicitacao': {'required': True, 'write_only': True},
            'usuario': {'required': True, 'write_only': True}
        }

    def validate_status(self, value):
        if not value:
            raise serializers.ValidationError("O status é obrigatório.")
        return value
    
    def validate(self, attrs):
        if not attrs.get('solicitacao'):
            raise serializers.ValidationError("A solicitação é obrigatória.")
        
        if not attrs.get('usuario'):
            raise serializers.ValidationError("O usuário é obrigatório.")
        return attrs
from rest_framework import serializers
from fluxoAprovacao.models import FluxoAprovacao, EtapaFluxo, Etapa

class FluxoAprovacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FluxoAprovacao
        fields = ['id', 'nome', 'descricao', 'data_criacao']
        extra_kwargs = {
            'descricao': {'required': False}
        }
    def validate_nome(self, value):
        if FluxoAprovacao.objects.filter(nome=value).exists():
            raise serializers.ValidationError("Este nome de fluxo já está em uso.")
        return value

class EtapaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields = ['id', 'nome', 'descricao', 'data_criacao']
        extra_kwargs = {
            'descricao': {'required': False}
        }
    def validate_nome(self, value):
        if Etapa.objects.filter(nome=value).exists():
            raise serializers.ValidationError("Este nome de etapa já está em uso.")
        return value

class EtapaFluxoSerializer(serializers.ModelSerializer):
    fluxo_aprovacao_nome = serializers.SerializerMethodField()
    etapa_nome = serializers.SerializerMethodField()
    etapa_anterior_nome = serializers.SerializerMethodField()

    class Meta:
        model = EtapaFluxo
        fields = ['id', 'fluxo_aprovacao', 'etapa', 'etapa_anterior', 'fluxo_aprovacao_nome', 'etapa_nome', 'etapa_anterior_nome']
        extra_kwargs = {
            'fluxo_aprovacao': {'required': True,
                                'write_only': True},
            'etapa': {'required': True,
                      'write_only': True},
            'etapa_anterior': {'required': False,
                      'write_only': True}
        }
    
    def get_fluxo_aprovacao_nome(self, obj):
        return obj.fluxo_aprovacao.nome if obj.fluxo_aprovacao else None
    def get_etapa_nome(self, obj):
        return obj.etapa.nome if obj.etapa else None
    def get_etapa_anterior_nome(self, obj):
        return obj.etapa_anterior.nome if obj.etapa_anterior else None
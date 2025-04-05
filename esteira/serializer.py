from rest_framework import serializers
from esteira.models import Esteira, EsteiraFluxo

class EsteiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Esteira
        fields = ['id', 'nome', 'descricao', 'data_criacao']
        extra_kwargs = {
            'descricao': {'required': False}
        }
    def validate_nome(self, value):
        if Esteira.objects.filter(nome=value).exists():
            raise serializers.ValidationError("Este nome de esteira já está em uso.")
        return value
class EsteiraFluxoSerializer(serializers.ModelSerializer):
    esteira_nome = serializers.SerializerMethodField()
    fluxo_aprovacao_nome = serializers.SerializerMethodField()

    class Meta:
        model = EsteiraFluxo
        fields = ['id', 'esteira', 'fluxo_aprovacao', 'esteira_nome', 'fluxo_aprovacao_nome']
        extra_kwargs = {
            'esteira': {'required': True,
                        'write_only': True},
            'fluxo_aprovacao': {'required': True,
                                'write_only': True}
        }
    
    def get_esteira_nome(self, obj):
        return obj.esteira.nome if obj.esteira else None
    def get_fluxo_aprovacao_nome(self, obj):
        return obj.fluxo_aprovacao.nome if obj.fluxo_aprovacao else None

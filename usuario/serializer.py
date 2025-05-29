from rest_framework import serializers
from usuario.models import Usuario, Grupo, Permissao, GrupoPermissao, UsuarioGrupo

class UsuarioSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True, source='password')
    
    class Meta:
        model = Usuario
        fields = ['id', 'nome_usuario', 'nome', 'email', 'senha', 'data_criacao']
        extra_kwargs = {
            'senha': {'write_only': True}
        }
    def validate_email(self, value):
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email já está em uso.")
        return value
    def validate_senha(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("A senha deve ter pelo menos 8 caracteres.")
        return value
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = Usuario(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo
        fields = ['id', 'nome', 'descricao']
        extra_kwargs = {
            'descricao': {'required': False}
        }
    def validate_nome(self, value):
        if Grupo.objects.filter(nome=value).exists():
            raise serializers.ValidationError("Este nome de grupo já está em uso.")
        return value

class PermissaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permissao
        fields = ['id', 'nome', 'descricao']
        extra_kwargs = {
            'descricao': {'required': False}
        }
    def validate_nome(self, value):
        if Permissao.objects.filter(nome=value).exists():
            raise serializers.ValidationError("Este nome de permissão já está em uso.")
        return value

class GrupoPermissaoSerializer(serializers.ModelSerializer):
    grupo_nome = serializers.SerializerMethodField()
    permissao_nome = serializers.SerializerMethodField()
    class Meta:
        model = GrupoPermissao
        fields = ['id', 'grupo', 'permissao', 'grupo_nome', 'permissao_nome']
        extra_kwargs = {
            'grupo': {'required': True,
                      'write_only': True},
            'permissao': {'required': True,
                          'write_only': True}
        }

    def get_grupo_nome(self, obj):
        return obj.grupo.nome if obj.grupo else None
    def get_permissao_nome(self, obj):
        return obj.permissao.nome if obj.permissao else None

class UsuarioGrupoSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.SerializerMethodField()
    grupo_nome = serializers.SerializerMethodField()
    class Meta:
        model = UsuarioGrupo
        fields = ['id', 'usuario', 'grupo', 'usuario_nome', 'grupo_nome']
        extra_kwargs = {
            'usuario': {'required': True,
                        'write_only': True},
            'grupo': {'required': True,
                      'write_only': True}
        }
    def get_usuario_nome(self, obj):
        return obj.usuario.nome if obj.usuario else None
    def get_grupo_nome(self, obj):
        return obj.grupo.nome if obj.grupo else None
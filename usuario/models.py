from django.db import models

# Create your models here.

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['nome']

class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        ordering = ['nome']

class Permissao(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Permissão'
        verbose_name_plural = 'Permissões'
        ordering = ['nome']

class GrupoPermissao(models.Model):
    id = models.AutoField(primary_key=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='permissoes')
    permissao = models.ForeignKey(Permissao, on_delete=models.CASCADE, related_name='grupos')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.grupo.nome} - {self.permissao.nome}"
    
    class Meta:
        verbose_name = 'Grupo Permissão'
        verbose_name_plural = 'Grupos Permissões'
        ordering = ['grupo__nome']

class UsuarioGrupo(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='grupos')
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='usuarios')
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.nome} - {self.grupo.nome}"
    class Meta:
        verbose_name = 'Usuário Grupo'
        verbose_name_plural = 'Usuários Grupos'
        ordering = ['usuario__nome']
        indexes = [
            models.Index(fields=['usuario', 'grupo']),
        ]
    def save(self, *args, **kwargs):
        if self.usuario and self.grupo:
            if not UsuarioGrupo.objects.filter(usuario=self.usuario, grupo=self.grupo).exists():
                super().save(*args, **kwargs)
        else:
            raise ValueError("Usuário e Grupo são obrigatórios.")
    def delete(self, *args, **kwargs):
        if self.usuario and self.grupo:
            super().delete(*args, **kwargs)
        else:
            raise ValueError("Usuário e Grupo são obrigatórios.")
    def get_permissions(self):
        return self.grupo.permissoes.all()
    def get_group_name(self):
        return self.grupo.nome
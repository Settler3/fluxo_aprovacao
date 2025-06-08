from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
# Create your models here.

class CustomUsuarioGerenciador(UserManager):
    def _create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        if not extra_fields.get('nome'):
            raise ValueError('Nome é obrigatório para superusuário')
        if not extra_fields.get('nome_usuario'):
            raise ValueError('Nome de usuário é obrigatório para superusuário')
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if not extra_fields.get('nome'):
            raise ValueError('Nome é obrigatório para superusuário')
        if not extra_fields.get('nome_usuario'):
            raise ValueError('Nome de usuário é obrigatório para superusuário')
        return self._create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    nome_usuario = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    grupo = models.ManyToManyField('Grupo', blank=True, related_name='usuarios')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    ultimo_login = models.DateTimeField(null=True, blank=True)

    objects = CustomUsuarioGerenciador()
    USERNAME_FIELD = 'nome_usuario'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['nome', 'email']

    def get_full_name(self):
        return self.nome
    
    def get_short_name(self):
        return self.nome or self.email.split('@')[0]
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['nome']

class Grupo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    permissoes = models.ManyToManyField('Permissao', blank=True, related_name='grupos')

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
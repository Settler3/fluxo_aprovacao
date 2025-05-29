from django.contrib import admin

# Register your models here.
from .models import Usuario, Grupo, Permissao, GrupoPermissao, UsuarioGrupo

admin.site.register(Usuario)
admin.site.register(Grupo)
admin.site.register(Permissao)
admin.site.register(GrupoPermissao)
admin.site.register(UsuarioGrupo)
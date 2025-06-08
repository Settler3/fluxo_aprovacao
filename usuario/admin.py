from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import Usuario, Grupo, Permissao

class UsuarioAdmin(UserAdmin):
    model = Usuario
    # Remova 'groups' e 'user_permissions' dos fieldsets e add_fieldsets
    fieldsets = (
        (None, {'fields': ('nome', 'nome_usuario', 'email', 'password')}),
        ('Informações pessoais', {'fields': ()}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Datas importantes', {'fields': ('ultimo_login',)}),
        ('Grupos customizados', {'fields': ('grupo',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('nome', 'nome_usuario', 'email', 'password1', 'password2', 'grupo', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    list_display = ('nome_usuario', 'email', 'is_staff', 'is_active')
    search_fields = ('nome_usuario', 'email')
    ordering = ('nome',)

    filter_horizontal = ('grupo',)

    # Remova os campos do Django padrão
    exclude = ('groups', 'user_permissions')


class GrupoAdmin(admin.ModelAdmin):
    model = Grupo
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)
    filter_horizontal = ('permissoes',)

class PermissaoAdmin(admin.ModelAdmin):
    model = Permissao
    list_display = ('nome',)
    search_fields = ('nome',)
    ordering = ('nome',)

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Permissao, PermissaoAdmin)
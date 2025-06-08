from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from usuario.models import Permissao

@receiver(post_migrate)
def sync_custom_permissions(sender, **kwargs):
    for perm in Permission.objects.all():
        Permissao.objects.get_or_create(
            nome=perm.codename,
            defaults={
                'descricao': perm.name
            }
        )
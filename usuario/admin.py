from django.contrib.admin import ModelAdmin, register
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from usuario.models import Rol

@register(Rol)
class MaterialRolAdmin(ModelAdmin):
    icon_name = 'person'

@register(Permission)
class MaterialPermAdmin(ModelAdmin):
    icon_name = 'lock'

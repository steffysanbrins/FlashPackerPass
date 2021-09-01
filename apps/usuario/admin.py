from django.contrib import admin
from apps.usuario.models import Usuario
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class UsuarioResource(resources.ModelResource):
    class meta:
        model = Usuario


class UsuariosAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ordering = ["id_user"]
    search_fields = ['rut_user']
    list_display = ('id_user', 'rut_user', 'nombre_user', 'email_user', 'rol_usuario', 'is_active')
    list_per_page = 1
    resource_class = UsuarioResource

admin.site.register(Usuario, UsuariosAdmin)
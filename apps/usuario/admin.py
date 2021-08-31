from django.contrib import admin
from apps.usuario.models import Usuario

# Register your models here.

class UsuariosAdmin(admin.ModelAdmin):
    search_fields = ['rut_user']
    list_display = ('rut_user','nombre_user', 'email_user', 'rol_usuario', 'is_active')

admin.site.register(Usuario, UsuariosAdmin)
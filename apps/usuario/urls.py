from django.urls import path
from django.contrib.auth.decorators import login_required
from apps.usuario.views import RegistrarUsuario, ListadoUsuario

from . import views#


urlpatterns = [
    path('listado_usuarios/', login_required(ListadoUsuario.as_view()), name = 'listar_usuarios'),
    #path('registrar_usuario/', RegistrarUsuario.as_view(), name = 'registrar_usuario'),
    path('registrar_usuario/', views.RegistrarUsuario, name = 'registrar_usuario'), #m
]


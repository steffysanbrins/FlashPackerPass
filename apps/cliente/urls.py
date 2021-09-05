from django.urls import path
from apps.cliente.views import RutasCliente

urlpatterns = [
    path('rutascliente', RutasCliente.as_view(), name = 'rutascliente'),
]

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from apps.usuario.forms import FormularioUsuario
from apps.usuario.models import Usuario

# Create your views here.

class ListadoUsuario(ListView):
    model = Usuario
    template_name = 'usuarios/listar_usuario.html'
    def get_queryset(self):
        return self.model.objects.filter(is_active = True)

class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'crear_usuario.html'
    success_url = reverse_lazy('index')
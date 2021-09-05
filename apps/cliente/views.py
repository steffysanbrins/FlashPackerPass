from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class RutasCliente(TemplateView):
    template_name = 'clientes/rutas.html'

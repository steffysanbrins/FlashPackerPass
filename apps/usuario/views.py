from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from apps.usuario.forms import FormularioUsuario
from apps.usuario.models import Usuario

from django import forms #Formularios de django
from django.shortcuts import render#para renderizar una pagina por medio de una funcion y no una clase
from django.shortcuts import redirect #para redireccionar a un link
from django.contrib.auth.hashers import make_password #Funcion que encripta contraseñas

# Create your views here.

class ListadoUsuario(ListView):
    model = Usuario
    template_name = 'usuarios/listar_usuario.html'
    def get_queryset(self):
        return self.model.objects.filter(is_active = True)

'''class RegistrarUsuario(CreateView):
    model = Usuario
    form_class = FormularioUsuario
    template_name = 'crear_usuario.html'
    success_url = reverse_lazy('index')'''


#La función reecupera el formulario de la pagina en una variable, valida que está correcto, si lo está y antes de guardarlo en la base de datos
#encripta la contraseña con make_password, la guarda en la base de datos y luego redirecciona a la página de inicio (index)
def RegistrarUsuario(request): 
    if request.method == "POST":
        user_form = FormularioUsuario(request.POST)#Recuperación de formulario
        rut_user = request.POST['rut_user']
        nombre_user = request.POST['nombre_user']
        email_user = request.POST['email_user']
        password = request.POST['password']

        if user_form.is_valid() :
            user = user_form.save(commit=False)
            user.password = make_password(password) #Encriptación de contraseña
            user.save()
            return redirect('index') #Redireccionamiento

    return render(request, 'crear_usuario.html', {'form': FormularioUsuario}) #Renderización de la pagina de registro
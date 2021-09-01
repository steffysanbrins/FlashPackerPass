from django import forms
from django.db.models.fields import CharField
from django.forms import fields, widgets
from apps.usuario.models import Usuario

class FormularioUsuario(forms.ModelForm): #Falta validar las contraseñas
    """
        Formulario de registro de un usuario en la base de datos
    
        Variables
            password1: contrasena
            password2: verificar contrasena 
    """
    
    password = forms.CharField(
        label = 'contrasena',
        widget = forms.PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder':'ingrese su contrasena',
                'id':'password',
                'required':'required',
            }
        )
    )

    password2 = forms.CharField(
        label = 'contrasena de confirmacion',
        widget = forms.PasswordInput(
            attrs = {
                'class':'form-control',
                'placeholder':'ingrese nuevamente su contrasena',
                'id':'password2',
                'required':'required',
            }
        )
    )

    class Meta:
        model = Usuario
        fields = ('rut_user','nombre_user', 'email_user', 'password')
        widgets = {
            'rut_user':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'rut del usuario',
                }
            ),
            'nombre_user':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'nombre del usuario'
                }
            ),
            'email_user':forms.EmailInput(
               attrs = {
                    'class':'form-control',
                    'placeholder':'correo electronico'
               }
            )
        }

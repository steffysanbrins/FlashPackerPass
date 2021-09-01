from django.db import models
#importamos abstractbaseuser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.

"""
class Usuario(models.Model):
    usuario = models.ForeignKey(OTHERMODEL, on_delete = models.CASCADE)

si nosotros creamos la clase de esta manera, estamos creando un modelo usuario a parte del 
que trae django, por ende, debemos crear una clave foranea para vincularla con el modelo user que se 
importa de la siguiente ruta 

from django.contrib.auth.models import User

y asi tendriamos la relacion con el modelo user que trae django y agregariamos los campos que nosotros queramos,
ya sea alguna fecha de nacimiento u otro campo.

Sin embargo, cuando queremos tomarlo desde 0 o vamos a sobrescribirlo por completo, seria como algo basico, 
no tendria mucho sentido, como por ejemplo, estariamos sobrescribiendo o reinventando la rueda, cosa que ya
tiene el framework implemetadas, cosa que no debemos llegar a ese extremo. Lo vamos hacer referente al modelo...

El framework trae un modelo llamado AbstractBaseUser que es una clase abstracta, base del cual hereda el modelo User django,
este tiene diversas caracteristicas o metodos, como por ejemplo, encriptacion de contrasenas

vamos a tomar esta clase llamada AbstractBaseUser, que es la base de diversas funciones que trabajan con un modelo en especifico que se 
va a definir y estas se pueden heredar a una clase que funciona como usuario (que es la que creamos) y asi nos ahorramos el tiempo
de tener que escribir codigos de seguridad en un nuevo modelo, y diversos otros codigos.

"""
#creamos un manager relacionado a un modelo usuario, un ejemplo de manager es el createsuperuser
#y para eso, importamos BaseUserManager
class UsuarioManager(BaseUserManager):
    #definimos dos funciones
    #una, permite crear un usuario basico
    def _create_user(self, rut_user, email_user, nombre_user, password, is_staff, is_superuser, **extra_fields):
        if not email_user:
            raise ValueError('El email debe ser obligatorio')
        email_user = self.normalize_email(email_user)
        usuario = self.model(
            rut_user = rut_user,
            email_user = email_user,
            nombre_user = nombre_user,
            is_active = True,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        usuario.set_password(password)
        usuario.save(using = self._db)
        return usuario
    def create_user(self, rut_user, email_user, nombre_user, password = None, **extra_fields):
        return self._create_user(rut_user, email_user, nombre_user, password, False, False, **extra_fields)

    def create_superuser(self, rut_user, email_user, nombre_user, password, **extra_fields):
        return self._create_user(rut_user, email_user, nombre_user, password, True, True, **extra_fields)


#idea de roles, cuando se cree una cuenta de usuario nueva, por defecto tendra la sesion activa en True, o sea, que puede iniciar sesion
#ademas, tendra el rol de cliente por defecto al momento de logearse

#idea sacada de portafolio y de youtube para continuar el registro
#investigar el pip install pillow.py

#heredamos el AbstractBaseUser en el modelo Usuario para definir los campos
class Usuario(AbstractBaseUser, PermissionsMixin):
    id_user = models.AutoField('ID usuario', auto_created = True, primary_key = True, serialize = False)
    rut_user = models.CharField('Rut del Usuario', unique = True, max_length = 50)
    perfil_user = models.ImageField('Imagen de Perfil', upload_to='perfil/', max_length=200, blank = True, null = True)
    nombre_user = models.CharField('Nombre del Usuario', max_length = 50)
    ape_paterno_user = models.CharField('Apellido Paterno', max_length = 100)
    ape_materno_user = models.CharField('Apellido Materno', max_length = 100)
    email_user = models.EmailField('Correo Electronico', unique = True, max_length = 255)
    is_active = models.BooleanField('Esta activo',default = True)
    is_staff = models.BooleanField('Es administrador',default = False)
    rol = (('socio', 'Socio'), ('cliente', 'Cliente'), ('guia', 'Guia'), ('trabajador', 'Trabajador'))
    rol_usuario = models.CharField(max_length=50, choices = rol, default = 'cliente')
    objects = UsuarioManager()

    USERNAME_FIELD = 'email_user' #hace referencia a cual es el parametro unico que va a diferenciar este usuario y que siempre sera requerido
    REQUIRED_FIELDS = ['rut_user','nombre_user'] #estos son los campos requeridos de forma obligatorio

    def __str__(self):
        return f'{self.nombre_user}, {self.ape_paterno_user}, {self.ape_materno_user}' #sintaxis de f string

    #lo que hace es que debe definirse para que AbstractBaseUser necesita diversas utilidades para que se pueda utilizar el modelo usuario en el admin django
    #es llamado por el admin django en la parte de los permisos de quien puede acceder o no al admin django
    #def has_perm(self, perm, obj = None):
    #    return True
    
    #esta funcion es para el admin django, ya que recibe la etiqueta de la aplicacion en la cual esta este modelo
    #def has_module_perms(self, app_label):
    #    return True

    #la funcion is_staff ya definida en el user natural django, y lo que hace es decir que si un usuario es administrador o no
    #@property
    #def is_staff(self):
    #    return self.user_administrador
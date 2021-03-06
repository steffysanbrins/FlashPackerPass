# Generated by Django 3.2.5 on 2021-08-30 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_user', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='User_ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('rut_user', models.CharField(max_length=50, unique=True, verbose_name='Rut del Usuario')),
                ('perfil_user', models.ImageField(blank=True, max_length=200, null=True, upload_to='perfil/', verbose_name='Imagen de Perfil')),
                ('nombre_user', models.CharField(max_length=50, verbose_name='Nombre del Usuario')),
                ('ape_paterno_user', models.CharField(max_length=100, verbose_name='Apellido Paterno')),
                ('ape_materno_user', models.CharField(max_length=100, verbose_name='Apellido Materno')),
                ('email_user', models.EmailField(max_length=255, unique=True, verbose_name='Correo Electronico')),
                ('user_active', models.BooleanField(default=True, verbose_name='Esta activo')),
                ('user_administrador', models.BooleanField(default=False, verbose_name='Es administrador')),
                ('rol_usuario', models.CharField(choices=[('socio', 'Socio'), ('cliente', 'Cliente'), ('guia', 'Guia'), ('trabajador', 'Trabajador')], default='cliente', max_length=50)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

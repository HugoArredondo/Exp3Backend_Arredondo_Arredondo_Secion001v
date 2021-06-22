from django.db import models

# Create your models here.
class Registro(models.Model):
    rutRegistro = models.IntegerField(primary_key=True, max_length=8, verbose_name='Rut')
    dvRegistro = models.CharField(max_length=1, verbose_name='Dígito Verificador')
    nombreRegistro = models.CharField(max_length=50, verbose_name='Nombre')
    apellidoRegistro = models.CharField(max_length=50, verbose_name='Apellido')
    fechaNacimientoRegistro = models.DateField(verbose_name='Fecha de Nacimiento')
    numContactoRegistro = models.IntegerField(max_length=8, verbose_name='Número de Contacto')
    correoRegistro = models.CharField(max_length=100, verbose_name='Correo Electrónico')
    nombreUsuarioRegistro = models.CharField(max_length=50, verbose_name='Nombre de Usuario')
    contraseñaRegistro = models.CharField(max_length=10, verbose_name='Contraseña')
    repetirContraseñaRegistro = models.CharField(max_length=10, verbose_name='Repetir Contraseña')

    def __str__(self):
        return self.nombreUsuarioRegistro

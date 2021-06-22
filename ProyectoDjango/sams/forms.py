from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Registro

class RegistroForm(forms.ModelForm):

    class Meta:
        model = Registro
        fields = [  'rutRegistro',
                    'dvRegistro',
                    'nombreRegistro',
                    'apellidoRegistro',
                    'fechaNacimientoRegistro',
                    'numContactoRegistro',
                    'correoRegistro',
                    'nombreUsuarioRegistro',
                    'contraseñaRegistro',
                    'repetirContraseñaRegistro'
        ]

        labels={
            'rutRegistro': 'Rut:',
            'dvRegistro': 'DV:',
            'nombreRegistro': 'Nombre:',
            'apellidoRegistro': 'Apellido:',
            'fechaNacimientoRegistro': 'Fecha de Nacimiento:',
            'numContactoRegistro': 'Número de Contacto (+569):',
            'correoRegistro': 'Correo Electrónico:',
            'nombreUsuarioRegistro': 'Nombre de Usuario:',
            'contraseñaRegistro': 'Contraseña:',
            'repetirContraseñaRegistro': 'Repitar Contraseña:'
        }

        widgets={
            'rutRegistro': forms.TextInput(
                attrs={
                    'id': 'rut',
                    'name': 'rut',
                    'placeholder': '11111111',
                    'onfocus': 'CambiaColor(this)',
                    'autofocus': True,
                    # 'required': True
                }
            ),
            'dvRegistro': forms.TextInput(
                attrs={
                    'id': 'dv',
                    'name': 'dv',
                    'placeholder': 'k',
                    'onfocus': 'CambiaColor(this)',
                    # 'required': True
                }
            ),
            'nombreRegistro': forms.TextInput(
                attrs={
                    'class': 'text-capitalize',
                    'id': 'name',
                    'name': 'name',
                    'placeholder': 'Ingrese su nombre',
                    'onfocus': 'CambiaColor(this)',
                    # 'required': True
                }
            ),
            'apellidoRegistro': forms.TextInput(
                attrs={
                    'class': 'text-capitalize',
                    'id': 'ap',
                    'name': 'ap',
                    'placeholder': 'Ingrese su apellido',
                    'onfocus': 'CambiaColor(this)',
                    # 'required': True
                }
            ),
            'fechaNacimientoRegistro': forms.DateInput(
                attrs={
                    'id': 'fecha',
                    'name': 'fecha',
                    'min': '1901-01-01',
                    'max': '2020-12-31',
                    # 'required': True
                }
            ),
            'numContactoRegistro': forms.TextInput(
                attrs={
                    'id': 'phone',
                    'name': 'phone',
                    'placeholder': '9999 9999',
                    'minlength':'8',
                    'onfocus': 'CambiaColor(this)',
                    # 'required': True
                }
            ),
            'correoRegistro': forms.EmailInput(
                attrs={
                    'id': 'email',
                    'name': 'email',
                    'placeholder': 'nombre@dominio.cl',
                    'onfocus': 'CambiaColor(this)',
                    # 'required': True
                }
            ),
            'nombreUsuarioRegistro': forms.TextInput(
                attrs={
                    'id': 'user',
                    'name': 'user',
                    'placeholder': 'Usuario',
                    'onfocus': 'CambiaColor(this)',
                    # 'required': True
                }
            ),
            'contraseñaRegistro': forms.PasswordInput(
                attrs={
                    'id': 'password',
                    'name': 'password',
                    'placeholder': 'Escribir contraseña',
                    'minlength':'8',
                    'onfocus': 'CambiaColor(this)',
                    # 'required': True
                }
            ),
            'repetirContraseñaRegistro': forms.PasswordInput(
                attrs={
                    'id': 'password2',
                    'name': 'password2',
                    'placeholder': 'Repetir contraseña',
                    'minlength':'8',
                    'onfocus': 'CambiaColor(this)',
                    # 'required': True
                }
            )
        }
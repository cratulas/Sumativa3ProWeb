from django import forms
from .models import ContactForm
from .models import Producto


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.forms import PasswordChangeForm

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

class ChangePasswordForm(PasswordChangeForm):
    pass    

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Escribe tu nombre de usuario'}))
    password = forms.PasswordInput(attrs={'placeholder': 'Escribe tu contraseña'})

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {
                'username': forms.TextInput(attrs={'placeholder': 'Escribe tu username'}),
                'email': forms.EmailInput(attrs={'placeholder': 'Escribe tu Email'}),
                'password1': forms.PasswordInput(attrs={'placeholder': 'Escribe tu contraseña'}),
                'password2': forms.PasswordInput(attrs={'placeholder': 'Confirma tu contraseña'}), 
            }
        error_messages = {
                'username': {
                    'required': 'El nombre de usuario es obligatorio.',
                    'unique': 'Este nombre de usuario ya está en uso. Por favor, elige otro.',
                    'invalid': 'El nombre de usuario contiene caracteres no permitidos.'
                },
                'email': {
                    'required': 'El correo electrónico es obligatorio.',
                    'unique': 'Este correo electrónico ya está registrado. ¿Ya tienes una cuenta?',
                    'invalid': 'Por favor, ingresa un correo electrónico válido.'
                },
                'password1': {
                    'required': 'La contraseña es obligatoria.',
                    'password_too_short': 'La contraseña es demasiado corta. Debe tener al menos 8 caracteres.',
                    'password_too_common': 'La contraseña es demasiado común. Por favor, elige una contraseña más compleja.',
                    'password_entirely_numeric': 'La contraseña no debe ser totalmente numérica.',
                },
                'password2': {
                    'required': 'La confirmación de la contraseña es obligatoria.',
                    'password_mismatch': 'Las contraseñas no coinciden. Por favor, asegúrate de que ambas sean idénticas.'
                },
            }

class ContactFormModel(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['nombre', 'email', 'telefono', 'website', 'asunto', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Escribe tu nombre'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Escribe tu Email'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Escribe tu teléfono'}),
            'website': forms.TextInput(attrs={'placeholder': 'Escribe la URL de tu web'}),
            'asunto': forms.TextInput(attrs={'placeholder': 'Escribe un asunto'}),
            'mensaje': forms.Textarea(attrs={'placeholder': 'Deja aquí tu comentario...'}),
        }
        error_messages = {
            'nombre': {
                'required': 'Este campo es obligatorio.',
            },
            'email': {
                'required': 'Este campo es obligatorio.',
            },
            'asunto': {
                'required': 'Este campo es obligatorio.',
            },
            'mensaje': {
                'required': 'Este campo es obligatorio.',
            },
        }
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
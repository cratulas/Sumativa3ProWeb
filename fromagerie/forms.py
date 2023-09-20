from django import forms
from .models import ContactForm

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

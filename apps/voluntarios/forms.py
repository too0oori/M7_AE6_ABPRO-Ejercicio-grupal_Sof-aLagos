from django import forms
from apps.voluntarios.models import Voluntario


class VoluntarioForm(forms.ModelForm):
    class Meta:
        model = Voluntario
        fields = ['nombre', 'email', 'telefono']

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'email': 'Email',
            'nombre': 'Nombre',
            'telefono': 'Teléfono',
        }

        error_messages = {
            'email': {
                'unique': 'Ya existe un voluntario con este email.',
            },
        }

        help_texts = {
            'email': 'Ingrese un email válido.',
            'telefono': 'Ingrese un número de teléfono válido.',
        }
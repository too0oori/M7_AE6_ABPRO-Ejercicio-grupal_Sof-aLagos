from django import forms
from apps.voluntarios.models import Voluntario
from apps.eventos.models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['titulo', 'descripcion', 'fecha']
        fields = ['titulo', 'descripcion', 'fecha', 'voluntarios']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese el título del evento.'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingrese la descripción del evento.', 'rows': 4}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'voluntarios': forms.CheckboxSelectMultiple(),
        }
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'fecha': 'Fecha',
            'voluntarios': 'Voluntarios Asignados',
        }

        error_messages = {
            'titulo': {
                'required': 'El título del evento es obligatorio.',
            },
            'descripcion': {
                'required': 'La descripción del evento es obligatoria.',
            },
            'fecha': {
                'required': 'La fecha del evento es obligatoria.',
            },
        }
    

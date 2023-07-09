from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_vencimiento', 'estado', 'etiqueta']
        
class ObservacionesForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['observaciones']
        widgets = {
            'observaciones': forms.Textarea(attrs={'rows': 5}),
        }
from django import forms
from .models import asesores

class form_Asesores(forms.ModelForm):

    class Meta:
        model = asesores
        fields =   ['nombres', 'usuario','email', ]
        widgets = {
            'nombres' :forms.TextInput(attrs={'class': 'form-control'}),
            'usuario' : forms.TextInput(attrs={'class': 'form-control'}),
            'email' : forms.TextInput(attrs={'class': 'form-control'}),
            
            
        }
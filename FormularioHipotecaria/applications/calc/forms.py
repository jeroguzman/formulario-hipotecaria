from django import forms
from .models import Banco, Actividad


class BancoUpdateForm(forms.ModelForm):


    class Meta:
        model = Banco
        fields = ('factor_millar',)
        widgets = {
            'factor_millar': forms.TextInput(attrs={'class': 'form-control'})
        }


class ActividadUpdateForm(forms.ModelForm):


    class Meta:
        model = Actividad
        fields = ('castigo', 'endeudamiento',)
        widgets = {
            'castigo': forms.TextInput(attrs={'class': 'form-control'}), 
            'endeudamiento': forms.TextInput(attrs={'class': 'form-control'})
        }


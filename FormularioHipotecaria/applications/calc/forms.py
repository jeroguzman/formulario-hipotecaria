from django import forms
from applications.users.models import Company
from .models import Banco, Actividad


class CompanyCreateForm(forms.ModelForm):


    class Meta:
        model = Company
        fields = ('name', 'logo')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'})
        }


class CompanyUpdateForm(forms.ModelForm):

    
    class Meta:
        model = Company
        fields = ('name', 'logo')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'})
        }


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


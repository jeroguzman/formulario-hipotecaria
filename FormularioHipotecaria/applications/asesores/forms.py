from django import forms
from .models import Asesores, Promotores

class form_Asesores(forms.ModelForm):

    class Meta():
        model = Asesores
        fields = ['nombre', 'usuario', 'email', 'pswd',]
        widgets = {
            'nombres' :forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre Completo' }),
            'usuario' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'pswd' : forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
        }
    
        labels = {
            'nombre':'', 'usuario':'', 'email':'', 'pswd':'' 
        }

class form_promotor(forms.ModelForm):
    
    class Meta():
        model = Promotores
        fields = [
            'nombre', 
            'usuario', 
            'telefono', 
            'email', 
            'empresa', 
            'asesor',
            'texto_bienvenida',
            'texto_despedida',
            'foto',
            'logo',
            'url', 
            'pswd',
        ]

        widgets = {
            'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
            'usuario' : forms.TextInput(attrs={'class': 'form-cotrol'}),
            'telefono' : forms.TextInput(attrs={'class': 'form-cotrol'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'empresa' : forms.TextInput(attrs={'class': 'form-cotrol'}),
            'asesor' : forms.Select(attrs={'class': 'form-control'}),
            'texto_bienvenida' : forms.TextInput(attrs={'class': 'form-control'}),
            'texto_despedida' : forms.TextInput(attrs={'class': 'form-control'}),
            'foto' : forms.FileInput(attrs={'class': 'form-control-file'}),
            'logo' : forms.FileInput(attrs={'class': 'form-control-file'}),
            'url' : forms.URLInput(attrs={'class': 'form-control'}),
            'pswd' : forms.PasswordInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'nombre' : '',
            'usuario' : '', 
            'telefono' : '', 
            'email' : '', 
            'empresa' : '', 
            'asesor' : '',
            'texto_bienvenida' : '',
            'texto_despedida' : '',
            'foto' : '',
            'logo' : '',
            'url' : '', 
            'pswd' : '',
        }

class form_dashboard(forms.ModelForm):
    
    class Meta():
        model = Promotores
        fields = [
            'nombre',
            'foto'
        ]
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
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'url' : forms.URLInput(attrs={'class': 'form-control'}),
            'asesor' : forms.TextInput(attrs={'class': 'form-control'}),
            'pswd' : forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class form_dashboard(forms.ModelForm):
    
    class Meta():
        model = Promotores
        fields = [
            'nombre',
            'foto'
        ]
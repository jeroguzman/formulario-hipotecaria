from django import forms
from .models import asesores

class form_Asesores(forms.ModelForm):

    class Meta():
        
        Puesto =[("Asesor", "Asesor"), ("Promotor", "Promotor")]
        model = asesores
        fields =   ['nombres', 'usuario','email', 'puesto', 'pswd',]
        widgets = {
            'nombres' :forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre Completo' }),
            'usuario' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Usuario'}),
            'email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'puesto' : forms.ChoiceField(choices=Puesto),
            'pswd' : forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),
    
        }
    
        labels = {
            'nombres':'', 'usuario':'', 'email':'', 'puesto':'', 'pswd':'' 
        },
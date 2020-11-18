from django import forms

class UserForm(forms.Form):
    tramite= forms.CharField(max_length=100)
    nombre= forms.CharField(max_length=100)
    correo= forms.EmailField()
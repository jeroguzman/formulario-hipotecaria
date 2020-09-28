from django import forms
from .models import asesores

class form_Asesores(forms.Form):

    # datos generales
    nombres = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control' }))
    usuario = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}))
    telefono = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}))
    email = forms.EmailField(widget = forms.TextInput(attrs = {'class': 'form-control' }))
    nclientes = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}))
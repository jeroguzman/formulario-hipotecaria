from django import forms


class form_asesor_alta(forms.Form):

    # datos generales
    nombres = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'Nombre' }))
    usuario = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}))
    telefono = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}))
    email = forms.EmailField(widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder':'email@example.com' }))
    nclientes = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}))
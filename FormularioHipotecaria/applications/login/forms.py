from django import forms

class form_login(forms.Form):
    user_name = forms.CharField(
        label='Nombre de usuario',
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Nombre de usuario'
        })
    )

    pswd = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Contraseña'
        })
    )

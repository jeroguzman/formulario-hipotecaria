from django import forms
from django.contrib.auth import authenticate
from .models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    confirm_password = forms.CharField(
        label='Confirmar Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )


    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'telefono',
            'modalidad',
            'asesor',
            'empresa',
            'bienvenida_txt',
            'despedida_txt',
            'foto',
            'url',
        )

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'modalidad': forms.Select(attrs={'id': 'modalidad', 'class': 'form-control promotor-field'}),
            'asesor': forms.HiddenInput(attrs={'class': 'form-control promotor-field'}),
            'empresa': forms.Select(attrs={'class': 'form-control promotor-field'}),
            'bienvenida_txt': forms.Textarea(attrs={'class': 'form-control promotor-field'}),
            'despedida_txt': forms.Textarea(attrs={'class': 'form-control promotor-field'}),
            'foto': forms.FileInput(attrs={'class': 'form-control promotor-field'}),
            'url': forms.HiddenInput(attrs={'class': 'form-control promotor-field'}),
        }

    def clean_confirm_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            self.add_error('confirm_password', 'Las contraseñas no coiciden')


class LoginForm(forms.Form):
    username = forms.CharField(
        label='',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de Usuario'
            }
        )
    )
    password = forms.CharField(
        label='',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Contraseña'
            }
        )
    )

    # def clean(self):
    #     cleaned_data = super(LoginForm, self).clean() 
    #     username = self.cleaned_data['username']
    #     password = self.cleaned_data['password']

    #     if not authenticate(username=username, password=password):
    #         raise forms.ValidationError('El nombre de usuario o la contraseña no coinciden')

    #     return self.cleaned_data


class UpdatePassForm(forms.Form):
    new_pass = forms.CharField(
        label='Nueva Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    confirm_new_pass = forms.CharField(
        label='Confirmar nueva contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    def clean_confirm_new_pass(self):
        if self.cleaned_data['new_pass'] != self.cleaned_data['confirm_new_pass']:
            self.add_error('confirm_new_pass', 'Las contraseñas no coinciden')
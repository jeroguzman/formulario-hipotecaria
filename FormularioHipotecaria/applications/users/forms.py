from django import forms
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
            'asesor': forms.TextInput(attrs={'class': 'form-control promotor-field'}),
            'bienvenida_txt': forms.Textarea(attrs={'class': 'form-control promotor-field'}),
            'despedida_txt': forms.Textarea(attrs={'class': 'form-control promotor-field'}),
            'foto': forms.FileInput(attrs={'class': 'form-control promotor-field'}),
            'url': forms.URLInput(attrs={'class': 'form-control promotor-field'}),
        }

    def clean_confirm_password(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            self.add_error('confirm_password', 'Las contraseñas no coinsiden')

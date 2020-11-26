from django import forms
from applications.users.models import Company


class CompanyCreateForm(forms.ModelForm):


    class Meta:
        model = Company
        fields = ('name', 'logo')


from applications.asesores.models import Asesores, Promotores
from django.views.generic.edit import FormView
from django.urls import reverse_lazy 
from .forms import form_login

# Create your views here.
class AuthUser(FormView):
    template_name = 'dashboard/shared/login.html'
    form_class = form_login
    success_url = reverse_lazy('home_app:a-dashboard')

    def form_valid(self, form):
        user = form.cleaned_data['user_name']
        field_pswd = form.cleaned_data['pswd']
        user_exists_as = Asesores.objects.filter(usuario=user).exists()
        user_exists_pr = Promotores.objects.filter(usuario=user).exists()

        if user_exists_as:
            if Asesores.objects.filter(pswd=field_pswd).exists():
                return super(AuthUser, self).form_valid(form)

        elif user_exists_pr:
            if Promotores.objects.filter(pswd=field_pswd).exists():
                return super(AuthUser, self).form_valid(form)
    

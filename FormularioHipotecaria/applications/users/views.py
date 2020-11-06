from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic import View
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, LoginForm
from .models import User

# Create your views here.
class UserRegisterView(FormView):
    template_name = 'dashboard/users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('a-dashboard')

    def form_valid(self, form):
        User.objects.create_user(
            form.cleaned_data['first_name'],
            form.cleaned_data['last_name'],
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['telefono'],
            form.cleaned_data['modalidad'],
            asesor=form.cleaned_data['asesor'],
            bienvenida_txt=form.cleaned_data['bienvenida_txt'],
            despedida_txt=form.cleaned_data['despedida_txt'],
            foto=form.cleaned_data['foto'],
            url=form.cleaned_data['url'],
        )

        return super(UserRegisterView, self).form_valid(form)


class LoginView(FormView):
    template_name = 'dashboard/users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:u-dashboard')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        print(user)
        login(self.request, user)

        return super(LoginView, self).form_valid(form)


class LogoutView(View):
    
    def get(self, request, *args, **kwargs):
        logout(request)
        
        return HttpResponseRedirect(
            reverse('users_app:u-login')
        )


class asesorListView(ListView):
    model = User
    form_class = UserRegisterForm
    template_name = 'dashboard/users/asesores_list.html'
    


class promotorListView(ListView):
    model = User
    form_class = UserRegisterForm
    template_name = 'dashboard/users/promotores_list.html'
    


class dashboardListView(ListView):
    model = User
    form_class = UserRegisterForm
    template_name = 'dashboard/dashboard.html'
    


from django.views.generic import (
    FormView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import (
    UserRegisterForm, 
    LoginForm, 
    UpdatePassForm
)
from .models import User

# Create your views here.
class UserRegisterView(LoginRequiredMixin, FormView):
    template_name = 'dashboard/users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:u-dashboard')
    login_url = reverse_lazy('users_app:u-login')

    def form_valid(self, form):
        user = User.objects.create_user(
            form.cleaned_data['first_name'],
            form.cleaned_data['last_name'],
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['telefono'],
            form.cleaned_data['modalidad'],
            asesor=self.request.user.username,
            bienvenida_txt=form.cleaned_data['bienvenida_txt'],
            despedida_txt=form.cleaned_data['despedida_txt'],
            foto=form.cleaned_data['foto'],
            url=form.cleaned_data['url'],
        )

        return super(UserRegisterView, self).form_valid(form)


class UserUpadateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'dashboard/users/edit.html'
    success_url = reverse_lazy('users_app:u-promotores')
    login_url = reverse_lazy('users_app:u-login')
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


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'dashboard/users/delete.html'
    success_url = reverse_lazy('users_app:u-promotores')
    login_url = reverse_lazy('users_app:u-login')


class LoginView(FormView):
    template_name = 'dashboard/users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('users_app:u-dashboard')

    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        login(self.request, user)

        return super(LoginView, self).form_valid(form)


class LogoutView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users_app:u-login')
    
    def get(self, request, *args, **kwargs):
        logout(request)
        
        return HttpResponseRedirect(
            reverse('users_app:u-login')
        )


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'dashboard/users/user.html'
    login_url = reverse_lazy('users_app:u-login')


class UserUpdatePassView(LoginRequiredMixin, FormView):
    model = User
    form_class = UpdatePassForm
    template_name = 'dashboard/users/update_pass.html'
    success_url = reverse_lazy('users_app:u-promotores')
    login_url = reverse_lazy('users_app:u-login')

    def form_valid(self, form):
        user = User.objects.get(pk=self.kwargs['pk'])
        user.set_password(form.cleaned_data['confirm_new_pass'])
        user.save()

        return super(UserUpdatePassView, self).form_valid(form)


class asesorListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'dashboard/users/asesores_list.html'
    login_url = reverse_lazy('users_app:u-login')


class promotorListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'dashboard/users/promotores_list.html'
    login_url = reverse_lazy('users_app:u-login')


class dashboardListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'dashboard/dashboard.html'
    login_url = reverse_lazy('users_app:u-login')

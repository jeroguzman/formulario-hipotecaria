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
    UpdatePassForm,
    UpdateUserForm
)
from .models import User

# Create your views here.
class UserRegisterView(LoginRequiredMixin, FormView):
    model = User
    template_name = 'dashboard/users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('home_app:a-dashboard')
    login_url = reverse_lazy('users_app:u-login')

    def form_valid(self, form): 
        user = User.objects.create_user(
            form.cleaned_data['first_name'],
            form.cleaned_data['last_name'],
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['telefono'],
            form.cleaned_data['password'],
            asesor=self.request.user.username,
            empresa=form.cleaned_data['empresa'],
            bienvenida_txt=form.cleaned_data['bienvenida_txt'],
            despedida_txt=form.cleaned_data['despedida_txt'],
            foto=form.cleaned_data['foto'],
            url=form.cleaned_data['url'],
        )
        user.modalidad = form.cleaned_data['modalidad']
        user.save()

        return super(UserRegisterView, self).form_valid(form)


class UserUpadateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'dashboard/users/edit.html'
    form_class = UpdateUserForm
    success_url = reverse_lazy('users_app:u-promotores')
    login_url = reverse_lazy('users_app:u-login')

    def form_valid(self, form):
        current_user = self.request.user
        user_to_edit = User.objects.filter(pk=self.kwargs['pk'], asesor=current_user.username)

        if user_to_edit.exists() or current_user.is_superuser:
            return super(UserUpadateView, self).form_valid(form)
        else:
            return HttpResponseRedirect(
                reverse('users_app:u-logout')
            )


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'dashboard/users/delete.html'
    success_url = reverse_lazy('users_app:u-promotores')
    login_url = reverse_lazy('users_app:u-login')


class LoginView(FormView):
    model = User
    template_name = 'dashboard/users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:a-dashboard')

    def form_valid(self, form):
        form_user = form.cleaned_data['username']
        form_pass = form.cleaned_data['password']

        user = authenticate(
            username=form_user,
            password=form_pass
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
        current_user = self.request.user
        user_to_edit = User.objects.filter(pk=self.kwargs['pk'], asesor=current_user.username)

        if current_user.is_superuser or user_to_edit.exists():
            user = User.objects.get(pk=self.kwargs['pk'])

            user.set_password(form.cleaned_data['new_pass'])
            user.save()

            return super(UserUpdatePassView, self).form_valid(form)
        else:
            return HttpResponseRedirect(
                reverse('users_app:u-login')
            )


class asesorListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'dashboard/users/asesores_list.html'
    login_url = reverse_lazy('users_app:u-login')
    paginate_by = 10

    def get_queryset(self):
        queryset = User.objects.filter(modalidad='Asesor')

        return queryset


class promotorListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'dashboard/users/promotores_list.html'
    login_url = reverse_lazy('users_app:u-login')
    paginate_by = 10

    def get_queryset(self):
        # Administrador
        if self.request.user.is_superuser: 
            queryset = User.objects.filter(modalidad='Promotor')

            return queryset
        else: # Asesor
            current_user = self.request.user.username            
            queryset = User.objects.filter(modalidad='Promotor', asesor=current_user)

            return queryset

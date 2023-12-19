from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
from account_module.forms import RegisterForm, LoginForm
from account_module.models import User, Staff


class RegisterView(CreateView):
    template_name = 'account_module/register_page.html'
    model = User
    fields = ['National_Id', 'password']
    success_url = reverse_lazy('register:login_page')

    def form_valid(self, form):
        if User.objects.filter(National_Id=form.cleaned_data['National_Id']).exists():
            form.add_error('National_Id', 'کاربر قبلا در سایت ثبت نام کرده است')

        else:
            user = User.objects.create_user(username=form.cleaned_data['National_Id'])
            user.is_active = True
            user.set_password(form.cleaned_data['password'])
            user.save()
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'account_module/login.html'
    next_page = reverse_lazy('home:room')


class StaffView(ListView):
    template_name = 'account_module/about.html'
    model = Staff


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home:room'))

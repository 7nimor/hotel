from django.contrib.auth import login
from django.http import Http404
from django.shortcuts import render, redirect
from user_panel_module.forms import EditUserForm
# Create your views here.
from django.urls import reverse
from django.views import View

from account_module.forms import RegisterForm, LoginForm
from account_module.models import User, Staff


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register_page.html', context)

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            national_id = register_form.cleaned_data.get('National_Id')
            password_user = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(National_Id=national_id).exists()

            if user:
                register_form.add_error('National_Id', 'کاربر قبلا در سایت ثبت نام کرده است')
            else:
                new_user = User(National_Id=national_id,
                                password=password_user,
                                username=national_id
                                )
                new_user.set_password(password_user)
                new_user.is_active = True
                new_user.save()

                return redirect(reverse('login_page'))

        context = {
            'register_form': register_form
        }
        return render(request, 'account_module/register_page.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            national_id = login_form.cleaned_data.get('National_Id')
            password_user = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(National_Id=national_id).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('National_Id', 'شما در سایت ثبت نام نکرده اید')
                is_password_correct = user.check_password(password_user)
                if is_password_correct:
                    login(request, user)
                    return redirect(reverse('edit_user_panel'))

        context = {
            'login_form': login_form
        }
        return render(request, 'account_module/login.html', context)


def staff(request):
    staff = Staff.objects.all()
    context = {
        'staff': staff
    }
    return render(request, 'account_module/about.html', context)

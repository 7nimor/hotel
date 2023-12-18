from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView
from account_module.forms import RegisterForm, LoginForm
from account_module.models import User, Staff


class RegisterView(CreateView):
    model = User
    template_name = 'account_module/register_page.html'
    fields = ['username', 'password', 'National_Id']
    success_url = reverse_lazy('register:login_page')

    def form_valid(self, form):
        if not User.objects.filter(National_Id=form.cleaned_data['National_Id']).exists():
            user = User.objects.create_user(National_Id=form.cleaned_data['National_Id'],
                                            username=form.cleaned_data['username'])
            user.is_active = True
            user.set_password(form.cleaned_data['password'])
            user.save()
        else:
            return form.dd_error('National_Id', 'کاربر قبلا در سایت ثبت نام کرده است')
        return super().form_valid(form)


# class RegisterView(View):
#     def get(self, request):
#         register_form = RegisterForm()
#         context = {
#             'register_form': register_form
#         }
#         return render(request, 'account_module/register_page.html', context)
#
#     def post(self, request):
#         register_form = RegisterForm(request.POST)
#         if register_form.is_valid():
#             national_id = register_form.cleaned_data.get('National_Id')
#             password_user = register_form.cleaned_data.get('password')
#             user: bool = User.objects.filter(National_Id=national_id).exists()
#
#             if user:
#                 register_form.add_error('National_Id', 'کاربر قبلا در سایت ثبت نام کرده است')
#             else:
#                 new_user = User(National_Id=national_id,
#                                 password=password_user,
#                                 username=national_id
#                                 )
#                 new_user.set_password(password_user)
#                 new_user.is_active = True
#                 new_user.save()
#
#                 return redirect(reverse('login_page'))
#
#         context = {
#             'register_form': register_form
#         }
#         return render(request, 'account_module/register_page.html', context)


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


class StaffView(ListView):
    template_name = 'account_module/about.html'
    model = Staff


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('register:logout_page'))

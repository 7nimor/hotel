from django import forms
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    National_Id = forms.CharField(
        max_length=10,
        label='کد ملی'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='پسورد'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(),
        label='تکرار پسورد'

    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        return ValidationError('کلمه عبور با تکرار آن مغایرت دارد')


class LoginForm(forms.Form):
    National_Id = forms.CharField(
        max_length=10,
        label='کد ملی'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='پسورد'
    )

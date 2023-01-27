from django import forms
from django.core.exceptions import ValidationError

from account_module.models import User


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'National_Id', 'phone_number', 'city', 'State']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'National_Id': forms.TextInput(
                attrs={
                    'class': 'form-control'
                },


            ),
            'State': forms.TextInput(
                attrs={
                    'class': 'form-control'
                },


            ),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control'
                },


            ),

            'phone_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                    'id': 'message',
                })
        }
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'National_Id': 'کد ملی',
            'phone_number': 'شماره تلفن'
        }


class ChangePasswordUserForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        label='پسورد قدیمی'
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        label='پسورد'
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        }),
        label='تکرار پسورد'

    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        return ValidationError('کلمه عبور با تکرار آن مغایرت دارد')

from django import forms
from django.forms import HiddenInput


class RoomForm(forms.Form):
    date_in = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            ),
        label='تاریخ ورود',
    )
    date_out = forms.DateField(
        widget=forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
            }
        ),
        label='تاریخ خروج', )

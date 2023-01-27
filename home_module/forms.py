from django import forms
from django.conf.global_settings import DATE_INPUT_FORMATS
from django.core.exceptions import ValidationError
from django.utils.datetime_safe import date



class RoomForm(forms.Form):

    number = forms.IntegerField(
        label='تعداد',
        max_value=5

    )
    date_in = forms.DateField(
        widget=forms.SelectDateWidget(),
        label='تاریخ ورود',
    )
    date_out = forms.DateField(
        widget=forms.SelectDateWidget(),
        label='تاریخ خروج',)

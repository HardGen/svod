
from django import forms


class OtdForm(forms.Form):
    lpu = forms.CharField(max_length=255)
    idotd = forms.IntegerField()
    otd_name = forms.CharField(max_length=255)
    short_otd = forms.CharField(max_length=255)
    activ = forms.BooleanField()
    zav_otd = forms.CharField(max_length=255)
    msister = forms.CharField(max_length=255)

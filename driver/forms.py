from django import forms
from .models import *


class DriverForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class DriversForm(forms.ModelForm):

    class Meta:
        model = Driver
        exclude = ['user', 'bio']


class RiderForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',)


class RiderForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = ('bio','phone','picture','username', 'email')
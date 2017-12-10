from django import forms
from .models import *


class DriverForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')


class DriversProfileForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = ( 'user','profile_pic','car_picture','number_plates', 'capacity','color','phone','city','vehicle_name','vehicle_model','bio')


class RidersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username',)


class RiderForm(forms.ModelForm):
    class Meta:
        model = Rider
        fields = ('bio','phone','picture','username', 'email')



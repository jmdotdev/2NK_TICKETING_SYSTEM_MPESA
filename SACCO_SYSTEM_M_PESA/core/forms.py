from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from bookings.models import Booking
from core.models import Car, Route
from drivers.models import Driver


class AddFriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        widgets = {
            'Username': forms.TextInput(attrs={'class': 'form-control'}),
            'First_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Second_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'ID_No': forms.TextInput(attrs={'class': 'form-control'}),
            'Avatar': forms.FileInput(),
            'Age': forms.NumberInput(attrs={'class': 'form-control'}),
            'feedback': forms.TextInput(attrs={'class': 'form-control'}),

        }
        fields = '__all__'


class ReserveSeatForm(forms.ModelForm):
    class Meta:
        model = Booking

        fields = ['date', 'Time', 'persons', 'mobile_no']


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'image', 'capacity', 'fuel',
                  'plate_no', 'Transmission', 'description'
                  ]


class AddRouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'


class AddBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

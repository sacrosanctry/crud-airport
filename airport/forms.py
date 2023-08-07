from django import forms
from airport.models import Passenger, Flight, Registration, Luggage, Interpol


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['name', 'passport', 'ticket', 'dem_register']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}),
                   'passport': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '9'}),
                   'ticket': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '9'}),
                   'dem_register': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '12'}),
                   }


# TODO required maxlength in edit html
class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['destination', 'departure_time', 'terminal', 'max_capacity']
        widgets = {'destination': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '100'}),
                   'departure_time': forms.DateTimeInput(attrs={'class': 'form-control'}), # 'format': '%d/%m/%Y %H:%M:%S'
                   'terminal': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '1'}),
                   'max_capacity': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '3'}),
                   }


# TODO passenger_id flight_id_id_id, check datatypes for prises
class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['passenger_id', 'flight_id', 'visa', 'price']
        widgets = {
                   #  'passenger_id': forms.NumberInput(attrs={'class': 'form-control'}),
                   # 'flight_id': forms.NumberInput(attrs={'class': 'form-control'}),
                   'visa': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': '9'}),
                   # 'luggage_price': forms.NumberInput(attrs={'class': 'form-control'}),
                   'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
                   # 'wanted': forms.NumberInput(attrs={'class': 'form-control'}),
                   }


# TODO registration_id
class LuggageForm(forms.ModelForm):
    class Meta:
        model = Luggage
        fields = ['registration_id', 'weight']
        widgets = {
            # 'registration_id': forms.NumberInput(attrs={'class': 'form-control'}),
                   'weight': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
                   }


class InterpolForm(forms.ModelForm):
    class Meta:
        model = Interpol
        fields = ['name', 'dem_register']
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'dem_register': forms.NumberInput(attrs={'class': 'form-control'}),
                   }

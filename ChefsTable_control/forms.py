from django import forms
from .models import Inputf, Reservation


class InputForm(forms.ModelForm):
    class Meta:
        model = Inputf
        fields = '__all__'
    
class Booking(forms.ModelForm):
    class Meta:
        model = Reservation
        fields ='__all__'
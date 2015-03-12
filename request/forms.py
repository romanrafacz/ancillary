from django.forms import ModelForm
from request.models import Room_Details
from functools import partial
from django import forms
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class RoomDetailsForm(ModelForm):
    class Meta:
        model = Room_Details
        fields = '__all__'
        widgets = { 'start_date': DateInput()}


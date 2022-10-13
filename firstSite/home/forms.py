from django.forms import ModelForm
from .models import Input, Goal
from django.forms import TextInput, NumberInput
# creating a form
class foodForm(ModelForm):
     class Meta:
         model = Input
         fields = '__all__'
         widgets = {
            'quantity': NumberInput(attrs={
                'class': 'form-control',
                'style': "min-width: 400px",
                'placeholder': "0",
            }),
            'unit': TextInput(attrs={
                'class': 'form-control',
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                "placeholder": "Food Type",
            }),
         }

class goalForm(ModelForm):
     class Meta:
         model = Goal
         fields = '__all__'
         
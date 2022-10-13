from django.forms import *
from .models import Input, Goal
# creating a form
class foodForm(ModelForm):
    class Meta:
        model = Input
        fields = '__all__'
        widgets = {
            'quantity': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "0",
            }),
            'unit': Select(attrs={
                'class': 'form-control',
                "placeholder": "Unit",
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
         widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
            }),
            'amount': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': "0",
            }),
            'measure': Select(attrs={
                'class': 'form-control',
                "placeholder": "Unit",
            }),
            'nutrient': Select(attrs={
                'class': 'form-control',
                "placeholder": "Nutrient Type",
            }),
            'progress': HiddenInput()
         }
         
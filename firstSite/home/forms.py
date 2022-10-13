from django.forms import ModelForm
from .models import Input
from django.forms import TextInput, NumberInput
# creating a form
class InputForm(ModelForm):
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
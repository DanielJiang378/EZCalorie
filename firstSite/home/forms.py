from django.forms import ModelForm
<<<<<<< HEAD
from .models import Input
from django.forms import TextInput, NumberInput
=======
from .models import *
>>>>>>> 70bdf6c406dbda9778aaa63610dd632cff488360
# creating a form
class foodForm(ModelForm):
     class Meta:
<<<<<<< HEAD
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
=======
         model = AddFood
         fields = '__all__'

class attrForm(ModelForm):
    class Meta:
        model = Food
        fields = '__all__'
>>>>>>> 70bdf6c406dbda9778aaa63610dd632cff488360

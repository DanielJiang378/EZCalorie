from django.forms import ModelForm
from .models import *
# creating a form
class foodForm(ModelForm):
     class Meta:
         model = AddFood
         fields = '__all__'
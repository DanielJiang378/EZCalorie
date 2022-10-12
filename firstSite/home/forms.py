from django.forms import ModelForm
from .models import Input
# creating a form
class InputForm(ModelForm):
     class Meta:
         model = Input
         fields = '__all__'
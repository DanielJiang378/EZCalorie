from django.db import models
UNIT_CHOICES = (
    ('grams','GRAMS'),
    ('lbs','POUNDS'),
    ('kilograms','KILOGRAMS')
)
# Create your models here.
class Input(models.Model):
    quantity = models.IntegerField()
    unit = models.CharField(max_length=9, choices=UNIT_CHOICES, default='grams')
    name = models.CharField(max_length=300)

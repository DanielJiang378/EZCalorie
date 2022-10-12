from django.db import models
UNIT_CHOICES = (
    ('grams','Grams'),
    ('lbs','Pounds'),
    ('kilograms','Kilograms')
)
# Create your models here.
class Input(models.Model):
    quantity = models.IntegerField()
    unit = models.CharField(max_length=9, choices=UNIT_CHOICES, default='grams')
    name = models.CharField(max_length=300)

class AddFood(models.Model):
    quantity = models.IntegerField()
    unit = models.CharField(max_length=9, choices=UNIT_CHOICES, default='grams')
    name = models.CharField(max_length=300)

    def __str__(self):
	    return self.name

class Food(models.Model):
        sugar = models.IntegerField()
        fiber = models.IntegerField()
        servingSize = models.IntegerField()
        sodium = models.IntegerField()
        
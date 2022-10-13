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
    sugar_g = models.IntegerField()
    fiber_g = models.IntegerField()
    serving_size_g = models.IntegerField()
    sodium_mg = models.IntegerField()
    name = models.CharField(max_length=100)
    potassium_mg = models.IntegerField()
    fat_saturated_g = models.IntegerField()
    fat_total_g = models.IntegerField()
    calories = models.IntegerField()
    cholesterol_mg = models.IntegerField()
    protein_g = models.IntegerField()
    carbohydrates_total_g = models.IntegerField()

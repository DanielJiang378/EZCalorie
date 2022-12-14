from contextlib import nullcontext
from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

UNIT_CHOICES = (
    ('grams','Grams'),
    ('lbs','Pounds'),
    ('kilograms','Kilograms')
)
UNIT_CHOICES2 = (
    ('grams','Grams'),
    ('lbs','Pounds'),
    ('kilograms','Kilograms'),
    ('kcal', 'Calories')
)
NUTRIENT_CHOICES = (
    ('calories','calories'),
    ('protein', 'protein_g')
)

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
    day = models.DateTimeField(auto_now_add=True, null=True)
    sugar_g = models.IntegerField(null=True)
    fiber_g = models.IntegerField(null=True)
    serving_size_g = models.IntegerField(null=True)
    sodium_mg = models.IntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    potassium_mg = models.IntegerField(null=True)
    fat_saturated_g = models.IntegerField(null=True)
    fat_total_g = models.IntegerField(null=True)
    calories = models.IntegerField(null=True)
    cholesterol_mg = models.IntegerField(null=True)
    protein_g = models.IntegerField(null=True)
    carbohydrates_total_g = models.IntegerField(null=True)

    def __str__(self):
        return str(self.name)

class Goal(models.Model):
    name = models.CharField(max_length = 100, null=True)
    amount = models.IntegerField(null=True)
    measure = models.CharField(max_length=9, choices=UNIT_CHOICES2, default='grams')
    nutrient = models.CharField(max_length=21, choices=NUTRIENT_CHOICES, default='calories')
    progress = models.FloatField(default=0, null=True)
    def __str__(self):
        return str(self.name)

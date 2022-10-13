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
        return self.name

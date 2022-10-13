from django.db import models
UNIT_CHOICES = (
    ('grams','Grams'),
    ('lbs','Pounds'),
    ('kilograms','Kilograms')
)
NUTRIENT_CHOICES = (
    ('sugar','sugar_g'),
    ('fiber','fiber_g'),
    ('serving_size','serving_size_g'),
    ('sodium','sodium_mg'),
    ('name','name'),
    ('potassium','potassium_mg'),
    ('fat_saturated','fat_saturated_g'),
    ('fat_total','fat_total_g'),
    ('calories','calories'),
    ('cholesterol','cholesterol_mg'),
    ('carbohydrates_total','carbohydrates_total_g'),
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
        return str(self.name)

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Goal(TimeStampMixin):
    name = models.CharField(max_length = 100, null=True)
    amount = models.IntegerField(null=True)
    measure = models.CharField(max_length=9, choices=UNIT_CHOICES, default='grams')
    nutrient = models.CharField(max_length=21, choices=NUTRIENT_CHOICES, default='sugar')
    def __str__(self):
        return str(self.name)

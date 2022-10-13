from contextlib import nullcontext
from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

UNIT_CHOICES = (
    ('grams','Grams'),
    ('lbs','Pounds'),
    ('kilograms','Kilograms')
)
NUTRIENT_CHOICES = (
    # ('sugar','sugar_g'),
    # ('fiber','fiber_g'),
    # ('serving_size','serving_size_g'),
    # ('sodium','sodium_mg'),
    # ('name','name'),
    # ('potassium','potassium_mg'),
    # ('fat_saturated','fat_saturated_g'),
    # ('fat_total','fat_total_g'),
    ('calories','calories'),
    # ('cholesterol','cholesterol_mg'),
    ('protein', 'protein_g')
    #('carbohydrates_total','carbohydrates_total_g'),
)

MONTH_CHOICES = (
    ('January'),
    ('February'),
    ('March'),
    ('April'),
    ('May'),
    ('June'),
    ('July'),
    ('August'),
    ('September'),
    ('October'),
    ('November'),
    ('December')
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

# class Date(models.Model):
#     # day = models.IntegerField(validators=[MaxValueValidator(30),MinValueValidator(1)](null=True))
#     # month = models.CharField(choices=MONTH_CHOICES, default='January',null=True)
#     # year = models.IntegerField(null=True)
#     day = models.CharField(max_length=5, null=True)
#     month = models.CharField(max_length=12, null=True)
#     year = models.CharField(max_length=12, null=True)

#     def __str__(self):
#         return self.month + "/" + self.day + "/" + self.year


class Food(models.Model):
    #day = models.ForeignKey(Date, null=True, on_delete=models.SET_NULL)
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

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Goal(TimeStampMixin):
    name = models.CharField(max_length = 100, null=True)
    amount = models.IntegerField(null=True)
    measure = models.CharField(max_length=9, choices=UNIT_CHOICES, default='grams')
    nutrient = models.CharField(max_length=21, choices=NUTRIENT_CHOICES, default='calories')
    def __str__(self):
        return str(self.name)

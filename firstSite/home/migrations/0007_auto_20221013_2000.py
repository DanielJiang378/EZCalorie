# Generated by Django 3.0.14 on 2022-10-14 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_goal_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='measure',
            field=models.CharField(choices=[('grams', 'Grams'), ('lbs', 'Pounds'), ('kilograms', 'Kilograms'), ('kcal', 'Calories')], default='grams', max_length=9),
        ),
    ]

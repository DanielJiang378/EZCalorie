# Generated by Django 3.0.14 on 2022-10-13 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(choices=[('grams', 'Grams'), ('lbs', 'Pounds'), ('kilograms', 'Kilograms')], default='grams', max_length=9)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sugar_g', models.IntegerField()),
                ('fiber_g', models.IntegerField()),
                ('serving_size_g', models.IntegerField()),
                ('sodium_mg', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('potassium_mg', models.IntegerField()),
                ('fat_saturated_g', models.IntegerField()),
                ('fat_total_g', models.IntegerField()),
                ('calories', models.IntegerField()),
                ('cholesterol_mg', models.IntegerField()),
                ('protein_g', models.IntegerField()),
                ('carbohydrates_total_g', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit', models.CharField(choices=[('grams', 'Grams'), ('lbs', 'Pounds'), ('kilograms', 'Kilograms')], default='grams', max_length=9)),
                ('name', models.CharField(max_length=300)),
            ],
        ),
    ]

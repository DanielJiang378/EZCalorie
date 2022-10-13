# Generated by Django 3.0.14 on 2022-10-13 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=5, null=True)),
                ('month', models.CharField(max_length=12, null=True)),
                ('year', models.CharField(max_length=12, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='day',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Date'),
        ),
    ]

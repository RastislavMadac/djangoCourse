# Generated by Django 5.2 on 2025-05-15 01:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(500)]),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-10 11:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnDjango', '0004_alter_room_floor_alter_room_rent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renthistory',
            name='totalRemaining',
            field=models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(999999.99)]),
        ),
        migrations.AlterField(
            model_name='renthistory',
            name='totalRequired',
            field=models.DecimalField(decimal_places=2, max_digits=8, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(999999.99)]),
        ),
        migrations.AlterField(
            model_name='rentpayment',
            name='paid',
            field=models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(9999.99)]),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-09 15:53

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learnDjango', '0002_person_rentpayment_room_floor_room_occupied_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NepaliDate',
            fields=[
                ('uid', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('month', models.CharField(default=' Unknown', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='rentpayment',
            old_name='amount',
            new_name='paid',
        ),
        migrations.RemoveField(
            model_name='rentpayment',
            name='rentMonth',
        ),
        migrations.AddField(
            model_name='person',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='person',
            name='roomId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='learnDjango.room'),
        ),
        migrations.AddField(
            model_name='rentpayment',
            name='personId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='learnDjango.person'),
        ),
        migrations.AddField(
            model_name='rentpayment',
            name='roomId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='learnDjango.room'),
        ),
        migrations.AddField(
            model_name='rentpayment',
            name='dateId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='learnDjango.nepalidate'),
        ),
        migrations.CreateModel(
            name='RentHistory',
            fields=[
                ('uid', models.AutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('totalRequired', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(999999.99)])),
                ('totalRemaining', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(999999.99)])),
                ('personId', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='learnDjango.person')),
                ('roomId', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='learnDjango.room')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='rentpayment',
            name='RentHistoryId',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='learnDjango.renthistory'),
        ),
    ]

# Generated by Django 4.0.8 on 2023-01-10 11:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0033_alter_booking_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

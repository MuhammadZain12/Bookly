# Generated by Django 4.0.8 on 2023-01-10 05:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0027_room_facilities'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='time',
            field=models.TimeField(default=datetime.datetime(2023, 1, 10, 5, 40, 7, 363237, tzinfo=utc)),
        ),
    ]

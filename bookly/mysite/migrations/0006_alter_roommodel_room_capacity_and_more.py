# Generated by Django 4.0.8 on 2022-12-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_hotelmodel_roommodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommodel',
            name='room_capacity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='roommodel',
            name='room_price',
            field=models.IntegerField(),
        ),
    ]
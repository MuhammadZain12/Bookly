# Generated by Django 4.0.8 on 2022-12-15 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_hotel_hotel_image2_hotel_hotel_image3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_image',
            field=models.ImageField(blank=True, upload_to='rooms'),
        ),
    ]
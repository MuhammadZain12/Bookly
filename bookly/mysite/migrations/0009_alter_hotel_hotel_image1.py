# Generated by Django 4.0.8 on 2022-12-15 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_rename_hotelmodel_hotel_rename_roommodel_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotel_image1',
            field=models.ImageField(blank=True, upload_to='hotels'),
        ),
    ]

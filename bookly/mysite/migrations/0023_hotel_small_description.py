# Generated by Django 4.0.8 on 2022-12-20 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0022_alter_hotel_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='small_description',
            field=models.TextField(default=models.CharField(max_length=25)),
        ),
    ]
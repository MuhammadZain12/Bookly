# Generated by Django 4.0.8 on 2022-12-16 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0012_alter_hotel_hotel_image1_alter_hotel_hotel_image2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_image1',
            new_name='image1',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_image2',
            new_name='image2',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_image3',
            new_name='image3',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_image4',
            new_name='image4',
        ),
        migrations.RenameField(
            model_name='hotel',
            old_name='hotel_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='room_capacity',
            new_name='capacity',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='room_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='room_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='room_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='room_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='room_type',
            new_name='type',
        ),
    ]

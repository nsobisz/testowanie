# Generated by Django 4.2.11 on 2024-03-27 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ListCars',
            new_name='Motor',
        ),
        migrations.RenameField(
            model_name='motor',
            old_name='imgCar',
            new_name='imgMotor',
        ),
        migrations.RenameField(
            model_name='motor',
            old_name='nameCar',
            new_name='nameMotor',
        ),
    ]

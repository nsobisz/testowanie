# Generated by Django 4.2.11 on 2024-04-24 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_motor_for_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='motor',
            name='color',
            field=models.CharField(default='white', max_length=100),
        ),
    ]
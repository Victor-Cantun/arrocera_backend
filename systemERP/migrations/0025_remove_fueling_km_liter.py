# Generated by Django 4.1 on 2023-02-09 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systemERP', '0024_fueling_hours_fueling_km_liter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fueling',
            name='km_liter',
        ),
    ]

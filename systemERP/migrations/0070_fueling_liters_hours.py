# Generated by Django 4.1 on 2023-05-06 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemERP', '0069_fueling_last_hours_unit_hours_worked_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fueling',
            name='liters_hours',
            field=models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=19, null=True, verbose_name='Kilometros/Litros'),
        ),
    ]

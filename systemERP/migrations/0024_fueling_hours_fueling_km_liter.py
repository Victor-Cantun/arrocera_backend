# Generated by Django 4.1 on 2023-02-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemERP', '0023_unit_c_verificationno_unit_pm_verificationno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='fueling',
            name='hours',
            field=models.DecimalField(decimal_places=2, max_digits=19, null=True, verbose_name='Horas Trabajas'),
        ),
        migrations.AddField(
            model_name='fueling',
            name='km_liter',
            field=models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=19, null=True, verbose_name='Kilometro/Litro'),
        ),
    ]

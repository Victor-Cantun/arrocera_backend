# Generated by Django 4.1 on 2023-05-23 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemERP', '0080_productbi_amount_productbi_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='paidplugins',
            name='document',
            field=models.FileField(null=True, upload_to='PaidPlugins/', verbose_name='Complementos de Pago'),
        ),
    ]
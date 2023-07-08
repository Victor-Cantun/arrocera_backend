# Generated by Django 4.1 on 2023-07-08 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemERP', '0095_shopping_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='producer',
            name='assigned_property',
            field=models.CharField(max_length=200, null=True, verbose_name='Predio asignado'),
        ),
        migrations.AddField(
            model_name='producer',
            name='curp',
            field=models.CharField(max_length=50, null=True, verbose_name='CURP'),
        ),
    ]

# Generated by Django 4.1 on 2023-07-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemERP', '0094_producer_observation'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopping',
            name='reason',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Reason'),
        ),
    ]

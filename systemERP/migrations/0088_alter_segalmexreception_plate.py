# Generated by Django 4.1 on 2023-05-31 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systemERP', '0087_plate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='segalmexreception',
            name='plate',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='systemERP.plate', verbose_name='Unidad'),
        ),
    ]

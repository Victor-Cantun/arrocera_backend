# Generated by Django 4.1 on 2023-03-27 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systemERP', '0045_payroll_hours_worked'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='systemERP.department'),
        ),
    ]

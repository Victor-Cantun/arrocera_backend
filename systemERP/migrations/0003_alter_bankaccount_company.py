# Generated by Django 4.1 on 2023-01-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemERP', '0002_alter_bankaccount_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='company',
            field=models.CharField(max_length=500, null=True, verbose_name='Empresa'),
        ),
    ]

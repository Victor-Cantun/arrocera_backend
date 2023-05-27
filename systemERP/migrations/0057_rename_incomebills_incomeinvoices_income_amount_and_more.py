# Generated by Django 4.1 on 2023-04-11 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemERP', '0056_remove_income_credit_note_remove_income_invoice_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IncomeBills',
            new_name='IncomeInvoices',
        ),
        migrations.AddField(
            model_name='income',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=19, null=True, verbose_name='Importe'),
        ),
        migrations.AddField(
            model_name='income',
            name='date',
            field=models.DateField(max_length=50, null=True, verbose_name='Fecha'),
        ),
    ]

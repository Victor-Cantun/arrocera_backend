# Generated by Django 4.1 on 2023-02-01 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systemERP', '0016_creditnote_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productquotation',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='systemERP.product'),
        ),
    ]

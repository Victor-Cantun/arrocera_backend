# Generated by Django 4.1 on 2023-05-20 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemERP', '0077_rename_productbilled_productbi_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditnote',
            name='no_creditnote',
            field=models.IntegerField(null=True, verbose_name='No. Nota de credito'),
        ),
    ]

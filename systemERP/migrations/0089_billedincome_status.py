# Generated by Django 4.1 on 2023-06-01 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemERP', '0088_alter_segalmexreception_plate'),
    ]

    operations = [
        migrations.AddField(
            model_name='billedincome',
            name='status',
            field=models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='Status'),
        ),
    ]

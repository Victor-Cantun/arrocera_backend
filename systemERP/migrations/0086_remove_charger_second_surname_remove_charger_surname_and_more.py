# Generated by Django 4.1 on 2023-05-29 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('systemERP', '0085_alter_segalmexreception_action_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charger',
            name='second_surname',
        ),
        migrations.RemoveField(
            model_name='charger',
            name='surname',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='second_surname',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='surname',
        ),
    ]

# Generated by Django 4.1 on 2023-06-02 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemERP', '0089_billedincome_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='users/NoPhoto.png', null=True, upload_to='employees/', verbose_name='Foto de perfil'),
        ),
    ]
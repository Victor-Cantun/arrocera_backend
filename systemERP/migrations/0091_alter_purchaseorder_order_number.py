# Generated by Django 4.1 on 2023-06-06 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systemERP', '0090_user_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='order_number',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Orden de pedido del cliente'),
        ),
    ]
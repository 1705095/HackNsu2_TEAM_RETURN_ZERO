# Generated by Django 3.1.1 on 2020-09-20 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_company_product_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_amount',
        ),
    ]
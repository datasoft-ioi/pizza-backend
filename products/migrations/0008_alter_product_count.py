# Generated by Django 4.2 on 2023-04-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_count_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]

# Generated by Django 4.2 on 2023-04-18 09:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_xit'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gramm',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]

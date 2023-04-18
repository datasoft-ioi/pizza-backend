# Generated by Django 4.2 on 2023-04-18 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_gramm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='info',
        ),
        migrations.AlterField(
            model_name='product',
            name='gramm',
            field=models.IntegerField(default=1),
        ),
    ]
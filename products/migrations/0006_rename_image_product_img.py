# Generated by Django 4.2 on 2023-04-18 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_description_product_info_alter_product_gramm'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image',
            new_name='img',
        ),
    ]

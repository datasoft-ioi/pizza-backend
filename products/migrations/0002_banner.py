# Generated by Django 4.2 on 2023-04-12 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=244)),
                ('image', models.ImageField(upload_to='banners/%Y/%m/%d')),
            ],
        ),
    ]

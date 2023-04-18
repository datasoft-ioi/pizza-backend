from django.db import models

from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')
    children = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='parent')

    class Meta:
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    xit = models.CharField(max_length=244)
    gramm = models.IntegerField(default=1)
    slug = models.SlugField(unique=True)
    info = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Banner(models.Model):
    title = models.CharField(max_length=244)
    image = models.ImageField(upload_to='banners/%Y/%m/%d')

    def __str__(self) -> str:
        return self.title

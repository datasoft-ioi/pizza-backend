from rest_framework import serializers
from .models import Category, Subcategory, Product, Banner, Basket


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'img', 'name', 'info', 'price', 'xit', 'gramm', 'count')
        depth = 1


class ChildrenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['name', 'slug']


class SubcategorySerializer(serializers.ModelSerializer):
    children = ChildrenSerializer()
    # products = ProductSerializer(many=True)

    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'slug', 'children', 'products')


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'subcategories')


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id','title', 'image']


class BasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = Basket
        fields = ('id', 'user', 'product', 'quantity', 'created_at', 'updated_at')

from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, CategoryDetail, SubcategoryViewSet, SubcategoryDetail, ProductList, ProductDetail, BannerViewSet

app_name = "products"

router = routers.DefaultRouter()
router.register(r'products', ProductList)
router.register(r'categories', CategoryViewSet)
router.register(r'subcategories', SubcategoryViewSet)
router.register(r'banners', BannerViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    # path('subcategdories/', SubcategoryViewSet, name='subcategory-list'),
    path('subcategories/<int:pk>/', SubcategoryDetail.as_view(), name='subcategory-detail'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
]
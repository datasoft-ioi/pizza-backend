from django.urls import path, include
from rest_framework import routers
from .views import (
    CategoryViewSet,CategoryDetail, SubcategoryViewSet,
    SubcategoryDetail, ProductList, ProductDetail, BannerViewSet, 
    CategoryProductListView, SubcategoryListCreateView, CategoryProductListView,
    SubcategoryProductListView, CategoryListCreateView, BasketListCreateAPIView, BasketDetailAPIView
)

app_name = "products"

router = routers.DefaultRouter()
router.register(r'products', ProductList)
router.register(r'categories/', CategoryViewSet)
# router.register(r'subcategories', SubcategoryViewSet)
router.register(r'banners', BannerViewSet)



urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryListCreateView.as_view()),
    # path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('categories/<int:category_id>/products/', CategoryProductListView.as_view()),
    # path('subcategdories/', SubcategoryViewSet, name='subcategory-list'),
    path('subcategories/<int:pk>/', SubcategoryDetail.as_view(), name='subcategory-detail'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='product-detail'),


    path('baskets/', BasketListCreateAPIView.as_view(), name='basket-list-create'),
    path('baskets/<int:pk>/', BasketDetailAPIView.as_view(), name='basket-detail'),
    
]

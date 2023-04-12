from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from . import views
from rest_framework import routers, serializers, viewsets


router = routers.DefaultRouter()
router.register(r'', views.UserSet)

app_name = 'users'

urlpatterns = [
    path('', include(router.urls)),
]


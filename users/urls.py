from django.urls import path, include
from rest_framework import routers, serializers, viewsets

from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


# router = routers.DefaultRouter()
# router.register(r'', views.UserSet)

app_name = 'users'

urlpatterns = [
    # path('', include(router.urls)),
    # path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/auth/register/', views.UserCreate.as_view(), name='register'),
    # path('register/', views.UserRegistrationView.as_view()),
    # path('register/', views.UserRegistrationView.as_view(), name='register'),
    # path('login/', views.UserLoginView.as_view(), name='login'),
    # path('logout/', views.UserLogoutView.as_view(), name='logout'),

    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='auth_register'),
    path('', views.getRoutes),


]


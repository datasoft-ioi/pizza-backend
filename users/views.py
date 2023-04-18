from django.shortcuts import render

# from .serializers import UserSerializer, CustomTokenObtainPairSerializer, UserRegisterSerializer

from .models import User

from rest_framework import routers, serializers, viewsets
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView


from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer



class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/users/token/',
        '/users/register/',
        '/users/token/refresh/'
    ]
    return Response(routes)

# class UserLoginView(generics.GenericAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]

#     @csrf_exempt
#     def post(self, request, *args, **kwargs):
#         username = request.data.get('username')
#         password = request.data.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'access': str(refresh.access_token),
#                 'refresh': str(refresh)
#             })
#         else:
#             return Response({'error': 'Invalid credentials'})


# class UserLogoutView(generics.GenericAPIView):
#     permission_classes = [permissions.IsAuthenticated]

#     @method_decorator(csrf_exempt)
#     def post(self, request, *args, **kwargs):
#         logout(request)
#         return Response({'success': 'Successfully logged out'})


# class UserRegistrationView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserRegisterSerializer
#     permission_classes = [permissions.AllowAny]


# class UserSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

   
# class UserCreate(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserRegisterSerializer





# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer
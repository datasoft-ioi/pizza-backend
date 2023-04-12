from django.shortcuts import render

from .serializers import UserSerializer

from .models import User

from rest_framework import routers, serializers, viewsets


class UserSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

   

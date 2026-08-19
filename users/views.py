from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import CustomUserSerializer


class RegisterCreateAPIView(CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes =[AllowAny]

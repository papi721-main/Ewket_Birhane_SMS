#!/usr/bin/env python3
from django.shortcuts import render
from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer

# Create your views here.


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "DELETE"]:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

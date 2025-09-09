#!/usr/bin/env python3
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Role, Batch, Department, Subject
from .serializers import UserSerializer, RoleSerializer, BatchSerializer, DepartmentSerializer, SubjectSerializer

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


class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserRoleAssignRemoveView(APIView):
    def post(self, request, pk):
        user = User.objects.get(pk=pk)
        role_id = request.data.get('role_id')
        role = Role.objects.get(pk=role_id)
        user.roles.add(role)
        return Response({'message': f'Role {role.name} assigned to user {user.username}'}, status=status.HTTP_200_OK)

    def delete(self, request, pk, role_id):
        user = User.objects.get(pk=pk)
        role = Role.objects.get(pk=role_id)
        user.roles.remove(role)
        return Response({'message': f'Role {role.name} removed from user {user.username}'}, status=status.HTTP_200_OK)


class BatchListCreateView(generics.ListCreateAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer


class BatchRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer


class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class SubjectListCreateView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

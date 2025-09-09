#!/usr/bin/env python3
"""
This module contains views for the core app.

Views handle HTTP requests and responses for the core app's models, including
User, Role, Batch, Department, and Subject. They provide endpoints for CRUD
operations and other business logic.
"""

from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Batch, Department, Role, Subject, User
from .serializers import (
    BatchSerializer,
    DepartmentSerializer,
    RoleSerializer,
    SubjectSerializer,
    UserSerializer,
)

# Create your views here.


class UserListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all users and creating a new user.

    - GET: Returns a list of all users.
    - POST: Creates a new user (admin-only access).
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Returns appropriate permissions based on the HTTP method.
        """
        if self.request.method == "POST":
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a user by ID.

    - GET: Retrieves a user by ID.
    - PUT: Updates a user by ID (admin-only access).
    - DELETE: Deletes a user by ID (admin-only access).
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Returns appropriate permissions based on the HTTP method.
        """
        if self.request.method in ["PUT", "DELETE"]:
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]


class RoleListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all roles and creating a new role.

    - GET: Returns a list of all roles.
    - POST: Creates a new role.
    """

    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class UserRoleAssignRemoveView(APIView):
    """
    Handles assigning and removing roles for a user.

    - POST: Assigns a role to a user.
    - DELETE: Removes a role from a user.
    """

    def post(self, request, pk):
        """
        Assigns a role to the user with the given primary key (pk).
        """
        user = User.objects.get(pk=pk)
        role_id = request.data.get("role_id")
        role = Role.objects.get(pk=role_id)
        user.roles.add(role)
        return Response(
            {"message": f"Role {role.name} assigned to user {user.username}"},
            status=status.HTTP_200_OK,
        )

    def delete(self, request, pk, role_id):
        """
        Removes the role with the given role_id from the user with the given primary key (pk).
        """
        user = User.objects.get(pk=pk)
        role = Role.objects.get(pk=role_id)
        user.roles.remove(role)
        return Response(
            {"message": f"Role {role.name} removed from user {user.username}"},
            status=status.HTTP_200_OK,
        )


class BatchListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all batches and creating a new batch.

    - GET: Returns a list of all batches.
    - POST: Creates a new batch.
    """

    queryset = Batch.objects.all()
    serializer_class = BatchSerializer


class BatchRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a batch by ID.

    - GET: Retrieves a batch by ID.
    - PUT: Updates a batch by ID.
    - DELETE: Deletes a batch by ID.
    """

    queryset = Batch.objects.all()
    serializer_class = BatchSerializer


class DepartmentListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all departments and creating a new department.

    - GET: Returns a list of all departments.
    - POST: Creates a new department.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentRetrieveUpdateDeleteView(
    generics.RetrieveUpdateDestroyAPIView
):
    """
    Handles retrieving, updating, and deleting a department by ID.

    - GET: Retrieves a department by ID.
    - PUT: Updates a department by ID.
    - DELETE: Deletes a department by ID.
    """

    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class SubjectListCreateView(generics.ListCreateAPIView):
    """
    Handles listing all subjects and creating a new subject.

    - GET: Returns a list of all subjects.
    - POST: Creates a new subject.
    """

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a subject by ID.

    - GET: Retrieves a subject by ID.
    - PUT: Updates a subject by ID.
    - DELETE: Deletes a subject by ID.
    """

    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class UserRetrieveByUsernameView(APIView):
    """
    Handles retrieving a user by their username.

    - GET: Retrieves a user by username.
    """

    def get(self, request, username):
        """
        Retrieves the user with the given username.
        """
        try:
            user = User.objects.get(username=username)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)


class UserManageByUsernameView(APIView):
    """
    Handles creating, updating, and deleting a user by their username.

    - POST: Creates a new user.
    - PUT: Updates an existing user.
    - DELETE: Deletes a user.
    """

    def post(self, request, username):
        """
        Creates a new user with the given username.
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, username):
        """
        Updates the user with the given username.
        """
        try:
            user = User.objects.get(username=username)
            serializer = UserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

    def delete(self, request, username):
        """
        Deletes the user with the given username.
        """
        try:
            user = User.objects.get(username=username)
            user.delete()
            return Response(
                {"message": "User deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=404)

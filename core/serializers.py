#!/usr/bin/env python3
"""
This module contains serializers for the core app models.

Serializers are used to convert complex data types, such as Django models,
into JSON or other content types for use in APIs. They also handle validation
and deserialization of input data.
"""

from rest_framework import serializers

from .models import Batch, Department, Role, Subject, User, User_Role


class RoleSerializer(serializers.ModelSerializer):
    """
    Serializer for the Role model.

    Converts Role instances into JSON and validates input data for Role creation or updates.
    """

    class Meta:
        model = Role
        fields = ["id", "name", "description"]


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the User model.

    Converts User instances into JSON and validates input data for User creation or updates.
    Includes nested RoleSerializer for user roles.
    """

    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
            "phone_number",
            "roles",
        ]


class BatchSerializer(serializers.ModelSerializer):
    """
    Serializer for the Batch model.

    Converts Batch instances into JSON and validates input data for Batch creation or updates.
    """

    class Meta:
        model = Batch
        fields = ["id", "name", "start_date", "end_date"]


class DepartmentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Department model.

    Converts Department instances into JSON and validates input data for Department creation or updates.
    """

    class Meta:
        model = Department
        fields = ["id", "name", "description"]


class SubjectSerializer(serializers.ModelSerializer):
    """
    Serializer for the Subject model.

    Converts Subject instances into JSON and validates input data for Subject creation or updates.
    """

    class Meta:
        model = Subject
        fields = ["id", "name", "code", "department"]

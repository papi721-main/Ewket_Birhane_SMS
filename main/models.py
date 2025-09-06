#!/usr/bin/env python3
from enum import unique

from django.db import models


class User(models.Model):
    """Model representing a user in the system."""

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)  # pyright: ignore
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Emergency_Contact(models.Model):
    """Model representing an emergency contact for a user."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Address(models.Model):
    """Model representing an address for a user or an emergency contact."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    emergency_contact = models.ForeignKey(
        Emergency_Contact, on_delete=models.CASCADE, null=True
    )
    street_address = models.CharField(max_length=255)
    woreda = models.IntegerField()
    sub_city = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Role(models.Model):
    """Model representing a role in the system."""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

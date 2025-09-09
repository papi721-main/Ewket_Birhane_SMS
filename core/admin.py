#!/usr/bin/env python3
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Batch, Role, User

# Customize admin page title
admin.site.site_header = "Ewket Birhane SMS Admin"
admin.site.site_title = "Ewket Birhane SMS Admin Portal"
admin.site.index_title = "Student Management System Administration"


# Customize User Admin Interface
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "usable_password",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "email",
                    "is_staff",
                    "date_of_birth",
                    "phone_number",
                ),
            },
        ),
    )


# Customize Role Admin Interface
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "created_at", "modified_at"]

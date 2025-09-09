#!/usr/bin/env python3
import datetime

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
    list_display = [
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
        "display_roles",
        "date_of_birth",
        "age",
        "is_staff",
        "phone_number",
    ]
    # list_editable = ["date_of_birth"]
    list_per_page = 25

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

    def age(self, user):
        """
        Custom method to calculate and display age.
        """
        today = datetime.date.today()
        age = (
            today.year
            - user.date_of_birth.year
            - (
                (today.month, today.day)
                < (user.date_of_birth.month, user.date_of_birth.day)
            )
        )
        return age

    def display_roles(self, user):
        """
        Custom method to display roles as a comma-separated string.
        """
        return ", ".join([role.name for role in user.roles.all()])

    display_roles.short_description = "Roles"


# Customize Role Admin Interface
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "created_at", "modified_at"]

#!/usr/bin/env python3
import datetime

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import (
    Batch,
    Course,
    Department,
    Role,
    Subject,
    User,
    Student_Profile,
    Teacher_Profile,
    Staff_Profile,
)

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


# Customize Batch Admin Interface
@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "start_date", "end_date", "description"]
    list_editable = ["level", "start_date", "end_date"]
    search_fields = ["name", "description"]
    list_filter = ["level", "start_date"]


# Customize Department Admin Interface
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "created_at", "modified_at"]
    list_editable = ["description"]
    search_fields = ["name", "description"]


# Customize Subject Admin Interface
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ["name", "department", "description", "created_at", "modified_at"]
    list_editable = ["department", "description"]
    search_fields = ["name", "description"]
    list_filter = ["department"]


# Customize Course Admin Interface
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["subject", "teacher", "batch", "semester", "year", "description"]
    list_editable = ["teacher", "batch", "semester", "year"]
    search_fields = ["subject__name", "description"]
    list_filter = ["semester", "year", "batch"]
    autocomplete_fields = ["subject", "teacher", "batch", "staff"]


# Customize Student_Profile Admin Interface
@admin.register(Student_Profile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "batch", "joined_at"]
    list_editable = ["batch", "joined_at"]
    search_fields = ["user__username", "batch__name"]
    list_filter = ["batch"]
    autocomplete_fields = ["user", "batch"]


# Customize Teacher_Profile Admin Interface
@admin.register(Teacher_Profile)
class TeacherProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "start_date", "remarks"]
    list_editable = ["start_date", "remarks"]
    search_fields = ["user__username", "remarks"]
    list_filter = ["start_date"]
    autocomplete_fields = ["user"]


# Customize Staff_Profile Admin Interface
@admin.register(Staff_Profile)
class StaffProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "start_date", "remarks"]
    list_editable = ["start_date", "remarks"]
    search_fields = ["user__username", "remarks"]
    list_filter = ["start_date"]
    autocomplete_fields = ["user"]

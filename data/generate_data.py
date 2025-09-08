#!/usr/bin/env python3
"""generate_data.py

This is a script for generating data using Django ORM

"""

import datetime
import os
import sys

import django

# Add module from parent directory
# ---
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
# ---

# Setup Django for this script
# ---
# 1. Tell Django where your settings module is
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "main.settings"
)  # adjust to your project

# 2. Setup Django
django.setup()

# ---

from demo_data import *

# 3. Now import models
from core.models import (
    Assessment,
    Batch,
    Course,
    Department,
    Emergency_Contact,
    Emergency_Contact_Address,
    Enrollment,
    Role,
    Staff_Profile,
    Student_Profile,
    Subject,
    Teacher_Profile,
    User,
    User_Address,
    User_Role,
)

# ---


def delete_all_data():
    """Removes all data from the database"""

    users = User.objects.filter(is_superuser=False)
    users.delete()

    for model in [
        Role,
        User_Role,
        Batch,
        Student_Profile,
        Staff_Profile,
        Teacher_Profile,
        Emergency_Contact,
        Emergency_Contact_Address,
        User_Address,
        Course,
        Enrollment,
        Assessment,
    ]:
        model.objects.all().delete()


def create_demo_roles():
    """Removes all previous roles and create fresh roles for a demo"""

    # Create demo roles
    Role.objects.bulk_create(demo_roles)

    # Check that it worked
    roles = Role.objects.all()
    print("Roles Created:")
    print("---------------")
    for role in roles:
        print(f"Role: {role.name} - {role.description}")
    print("---------------")


def create_demo_batches():
    """Create fresh batches for demo"""

    # Create demo batches
    Batch.objects.bulk_create(demo_batches)

    # Check that it worked
    batches = Batch.objects.all()
    print("Batches Created:")
    print("----------------------")
    for batch in batches:
        print(f"Batch: {batch.name} - {batch.level} - {batch.start_date}")
    print("----------------------")


def create_demo_student_users():
    """Creates fresh student users for a demo"""

    # Create student users
    User.objects.bulk_create(demo_student_users)

    # Assign "Student" roles, student profile and batch to student users
    student_role = Role.objects.get(name="Student")
    demo_batches_len = len(demo_batches)
    for i, user in enumerate(demo_student_users):
        user.roles.add(student_role)
        user.student_profile = Student_Profile.objects.create(user=user)
        user.student_profile.batch = demo_batches[i % demo_batches_len]
        user.student_profile.save()


def create_demo_users():
    """Removes all previous users and create fresh users for a demo"""

    # Call functions
    create_demo_student_users()

    # Check that it worked
    users = User.objects.all()
    print("Users Created:")
    print("----------------------")
    for user in users:
        print(
            f"User: {user.username} - {user.email} - {[role.name for role in user.roles.all()]}"
        )
    print("----------------------")


if __name__ == "__main__":
    delete_all_data()

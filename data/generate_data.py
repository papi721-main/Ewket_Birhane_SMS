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
    print("Creating roles")
    print("---------------")
    Role.objects.bulk_create(demo_roles)

    # Check that it worked
    roles = Role.objects.all()
    if not roles.exists():
        print("No roles were created")
        print("---------------")
        return

    print("Roles Created:")
    for role in roles:
        print(f"Role: {role.name} - {role.description}")
    print("---------------")


def create_demo_users():
    """Create fresh users for a demo"""

    # Create all users
    print("Creating users")
    print("----------------------")
    all_demo_users = demo_student_users + demo_staff_users + demo_teacher_users
    User.objects.bulk_create(all_demo_users)

    # Check that it worked
    users = User.objects.all()
    if not users.exists():
        print("No users were created")
        print("----------------------")
        return

    print("Users Created:")
    for user in users:
        print(
            f"User: {user.username} - {user.email} - {[role.name for role in user.roles.all()]}"
        )
    print("----------------------")


def assign_demo_roles():
    """Assign roles to users"""

    # Check that roles exist
    print("Assigning roles to users")
    print("------------------------")
    try:
        student_role = Role.objects.get(name="Student")
        teacher_role = Role.objects.get(name="Teacher")
        staff_role = Role.objects.get(name="Staff")
    except Role.DoesNotExist:
        print("Demo roles not found")
        print("------------------------")
        return

    # Assign student roles
    student_users = User.objects.filter(username__startswith="student")
    if not student_users.exists():
        print("No student users found")
    else:
        for student_user in student_users:
            student_user.roles.add(student_role)

    # Assign teacher roles
    teacher_users = User.objects.filter(username__startswith="teacher")
    if not teacher_users.exists():
        print("No teacher users found")
    else:
        for teacher_user in teacher_users:
            teacher_user.roles.add(teacher_role)

    # Assign staff roles
    staff_users = User.objects.filter(username__startswith="staff")
    if not staff_users.exists():
        print("No staff users found")
    else:
        for staff_user in staff_users:
            staff_user.roles.add(staff_role)

    # Check that it worked
    print("Roles assigned to users")
    for user in User.objects.all():
        print(
            f"User: {user.username} - {[role.name for role in user.roles.all()]}"
        )
    print("------------------------")


def create_demo_batches():
    """Create fresh batches for demo"""

    # Create demo batches
    print("Creating batches")
    print("----------------------")
    Batch.objects.bulk_create(demo_batches)

    # Check that it worked
    batches = Batch.objects.all()
    if not batches.exists():
        print("No batches were created")
        print("----------------------")
        return

    print("Batches Created:")
    for batch in batches:
        print(f"Batch: {batch.name} - {batch.level} - {batch.start_date}")
    print("----------------------")


def create_demo_student_profiles():
    """Creates student profiles"""

    print("Creating student profiles")
    print("------------------------")
    student_users = User.objects.filter(username__startswith="student")
    if not student_users.exists():
        print("No student users found")
        print("------------------------")
        return

    batches = Batch.objects.all()
    if not batches.exists():
        print("No batches found")
        print("------------------------")
        return

    batches_list = list(batches)
    demo_batches_len = len(batches_list)
    for i, user in enumerate(student_users):
        user.student_profile = Student_Profile.objects.create(user=user)
        user.student_profile.batch = demo_batches[i % demo_batches_len]
        user.student_profile.save()

    # Check that it worked
    print("Student Profiles Created:")
    for student in student_users:
        print(
            f"Student: {student.username} - {student.first_name} {student.last_name} - {student.student_profile.batch.name}"
        )
    print("------------------------")


def create_demo_teacher_profiles():
    """Creates teacher profiles"""

    print("Creating teacher profiles")
    print("------------------------")
    teacher_users = User.objects.filter(username__startswith="teacher")
    if not teacher_users.exists():
        print("No teacher users found")
        print("------------------------")
        return

    for user in teacher_users:
        Teacher_Profile.objects.create(user=user)

    # Check that it worked
    print("Teacher Profiles Created:")
    for teacher in teacher_users:
        print(
            f"Teacher: {teacher.username} - {teacher.first_name} {teacher.last_name} - {teacher.teacher_profile.created_at}"
        )
    print("------------------------")


def create_demo_staff_profiles():
    """Creates staff profiles"""

    print("Creating staff profiles")
    print("------------------------")
    staff_users = User.objects.filter(username__startswith="staff")
    if not staff_users.exists():
        print("No staff users found")
        print("------------------------")
        return

    for user in staff_users:
        Staff_Profile.objects.create(user=user)

    # Check that it worked
    print("Staff Profiles Created:")
    for staff in staff_users:
        print(
            f"Staff: {staff.username} - {staff.first_name} {staff.last_name} - {staff.staff_profile.created_at}"
        )
    print("------------------------")


def assign_user_addresses():
    """Assigns user addresses"""

    print("Assigning user addresses")
    print("------------------------")
    # Example data pools
    sub_cities = [
        "Bole",
        "Lemi Kura",
        "Yeka",
        "Kirkos",
        "Nifas Silk-Lafto",
        "Arada",
        "Kolfe Keranio",
        "Gullele",
        "Lideta",
        "Akaki Kality",
        "Addis Ketema",
    ]
    cities = [
        "Addis Ababa",
        "Adama",
        "Bahir Dar",
        "Mekelle",
        "Hawassa",
        "Dire Dawa",
        "Gondar",
        "Jimma",
        "Harar",
        "Debre Markos",
    ]

    users = User.objects.filter(is_superuser=False).order_by("id")
    if not users.exists():
        print("No users found")
        print("------------------------")
        return

    addresses = []
    for i, user in enumerate(users, start=1):
        addresses.append(
            User_Address(
                user=user,
                street_address=f"{100 + i} Main St",
                woreda=(i % 15) + 1,  # woreda cycles 1–15
                sub_city=sub_cities[i % len(sub_cities)],
                city=cities[i % len(cities)],
                country="Ethiopia",
            )
        )

    User_Address.objects.bulk_create(addresses)

    # Check that it worked
    user_addresses = User_Address.objects.all()
    if not user_addresses.exists():
        print("No user addresses were created")
        print("------------------------")
        return

    print("User Addresses Created:")
    for address in user_addresses:
        print(
            f"User: {address.user.username} - {address.street_address} - {address.city} - {address.country}"
        )
    print("------------------------")


if __name__ == "__main__":
    delete_all_data()
    create_demo_roles()
    create_demo_users()
    assign_demo_roles()
    create_demo_batches()
    create_demo_student_profiles()
    create_demo_teacher_profiles()
    create_demo_staff_profiles()
    assign_user_addresses()

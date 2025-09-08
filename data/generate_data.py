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
        Department,
        Subject,
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


def create_departments_and_subjects():
    # 1) Departments
    print("Creating departments")
    print("----------------------")
    dept_payload = [
        Department(
            name="Geez", description="Studies in the Ge'ez language and texts."
        ),
        Department(
            name="Dogmatic Theology",
            description="Core doctrines and theological studies.",
        ),
        Department(
            name="Biblical Studies",
            description="Old and New Testament studies.",
        ),
        Department(
            name="Church History",
            description="Historical development of the Church.",
        ),
    ]

    Department.objects.bulk_create(dept_payload)

    # Check if it worked
    departments = Department.objects.all()
    if not departments.exists():
        print("No departments were created")
        print("----------------------")
        return

    print("Departments Created:")
    for department in departments:
        print(f"Department: {department.name} - {department.description}")
    print("----------------------")

    # Fetch (including existing) for foreign-key mapping
    print("Creating subjects")
    print("----------------------")
    dept_map = {d.name: d for d in departments}

    # 2) Subjects (department_name, subject_name, description)
    subject_rows = [
        # Geez
        ("Geez", "Geez I", "Introductory Ge'ez reading and grammar."),
        ("Geez", "Geez II", "Intermediate Ge'ez syntax and translation."),
        ("Geez", "Geez III", "Advanced Ge'ez texts and commentary."),
        # Dogmatic Theology
        (
            "Dogmatic Theology",
            "Introduction to Dogmatic Theology",
            "Survey of dogmatic method and sources.",
        ),
        (
            "Dogmatic Theology",
            "Theological Ethics",
            "Moral theology grounded in doctrine.",
        ),
        (
            "Dogmatic Theology",
            "Theological Philosophy",
            "Philosophical foundations for theology.",
        ),
        # Biblical Studies
        (
            "Biblical Studies",
            "Introduction to Old Testament",
            "Overview, canon, themes of the OT.",
        ),
        (
            "Biblical Studies",
            "Introduction to New Testament",
            "Overview, canon, themes of the NT.",
        ),
        (
            "Biblical Studies",
            "Scriptural Studies",
            "Methods of interpretation and exegesis.",
        ),
        # Church History
        (
            "Church History",
            "Church History I",
            "Early Church to pre-medieval developments.",
        ),
        (
            "Church History",
            "Church History II",
            "Medieval to Reformation movements.",
        ),
        (
            "Church History",
            "Church History III",
            "Modern era to contemporary Church.",
        ),
    ]

    subjects_payload = [
        Subject(
            department=dept_map[dept_name], name=subj_name, description=desc
        )
        for (dept_name, subj_name, desc) in subject_rows
    ]
    Subject.objects.bulk_create(subjects_payload)

    # Check if it worked
    subjects = Subject.objects.all()
    if not subjects.exists():
        print("No subjects were created")
        print("----------------------")
        return

    print("Subjects Created:")
    for subject in subjects:
        print(
            f"Subject: {subject.department.name} - {subject.name} - {subject.description}"
        )
    print("----------------------")


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
    create_departments_and_subjects()

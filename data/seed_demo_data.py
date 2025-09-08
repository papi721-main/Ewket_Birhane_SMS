#!/usr/bin/env python3
"""seed_demo_data.py

This is a standalone Django script used for seeding mock data
using Django ORM to use for development and testing purposes.

The mock data is generated for the following models:
- User (100 students, 10 teachers, 5 staff)
- Role (3 roles)
- User_Role (assigned roles to users)
- User_Address (assigned addresses to users)
- Batch (4 batches)
- Student_Profile (assigned to student users)
- Staff_Profile (assigned to staff users)
- Teacher_Profile (assigned to teacher users)
- Department (4 departments)
- Subject (12 subjects, 3 per department)

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


def seed_demo_roles():
    """Removes all previous roles and create fresh roles for a demo"""

    # Create demo roles
    print("Creating roles")
    print("---------------")

    demo_roles = [
        Role(pk=1, name="Student", description="A student in the school"),
        Role(pk=2, name="Teacher", description="A teacher in the school"),
        Role(
            pk=3,
            name="Staff",
            description="A member of the school serving as a staff",
        ),
    ]

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


def seed_demo_users():
    """Create fresh users for a demo"""

    # Create all users
    print("Creating users")
    print("----------------------")

    demo_student_users = [
        User(
            username=f"student{i}",
            password="Password#123",
            first_name=first,
            last_name=last,
            date_of_birth=datetime.date(
                1990 + i % 10, (i % 12) + 1, (i % 28) + 1
            ),
            email=f"{first.lower()}.{last.lower()}@example.com",
            phone_number=f"+251911000{i:02d}",
            is_active=True,
        )
        for i, (first, last) in enumerate(
            [
                ("Abel", "Kebede"),
                ("Marta", "Teshome"),
                ("Samuel", "Bekele"),
                ("Hana", "Wolde"),
                ("Dawit", "Abebe"),
                ("Ruth", "Mengistu"),
                ("Solomon", "Tesfaye"),
                ("Sofia", "Getachew"),
                ("Yonatan", "Demissie"),
                ("Mahi", "Girma"),
                ("Nahom", "Haile"),
                ("Rahel", "Mekonnen"),
                ("Kaleab", "Zewdu"),
                ("Saron", "Abate"),
                ("Binyam", "Eshete"),
                ("Mimi", "Yohannes"),
                ("Henok", "Tadese"),
                ("Lily", "Alemu"),
                ("Natnael", "Gebremariam"),
                ("Betelhem", "Shiferaw"),
                ("Michael", "Abera"),
                ("Liya", "Tesfahun"),
                ("Yonas", "Asfaw"),
                ("Selam", "Kassahun"),
                ("Brook", "Hailemariam"),
                ("Tsion", "Molla"),
                ("Bereket", "Kebede"),
                ("Mahi", "Solomon"),
                ("Abenezer", "Worku"),
                ("Helen", "Yilma"),
                ("Kalkidan", "Fikru"),
                ("Dagmawit", "Adamu"),
                ("Fitsum", "Gizaw"),
                ("Eden", "Mekonnen"),
                ("Ashenafi", "Belay"),
                ("Meaza", "Bekele"),
                ("Rediet", "Taye"),
                ("Daniel", "Aberra"),
                ("Sosina", "Mengesha"),
                ("Robel", "Kassaye"),
                ("Sara", "Abay"),
                ("Biruk", "Tilahun"),
                ("Yeshi", "Tesfaye"),
                ("Amanuel", "Hagos"),
                ("Tigist", "Alemayehu"),
                ("Kebede", "Abebe"),
                ("Mulu", "Getaneh"),
                ("Meskerem", "Habte"),
                ("Habtamu", "Dereje"),
                ("Eyerusalem", "Ayalew"),
                ("Kidus", "Haile"),
                ("Meron", "Fekadu"),
                ("Nahom", "Shibeshi"),
                ("Meklit", "Endale"),
                ("Yohannes", "Zerihun"),
                ("Rahel", "Nigussie"),
                ("Mikiyas", "Abayneh"),
                ("Bethel", "Hailu"),
                ("Henok", "Desalegn"),
                ("Sena", "Gebru"),
                ("Tsehay", "Mamo"),
                ("Amare", "Eshetu"),
                ("Blen", "Mebratu"),
                ("Natnael", "Fisseha"),
                ("Eleni", "Abraham"),
                ("Hirut", "Getahun"),
                ("Fikirte", "Lulseged"),
                ("Sileshi", "Baye"),
                ("Yodit", "Gebeyehu"),
                ("Haftamu", "Tsegaye"),
                ("Aster", "Workneh"),
                ("Addis", "Kiros"),
                ("Kassahun", "Belachew"),
                ("Lemlem", "Tesfamariam"),
                ("Mengistu", "Haftu"),
                ("Hanna", "Guta"),
                ("Tamrat", "Ayana"),
                ("Tsedey", "Demeke"),
                ("Sintayehu", "Abera"),
                ("Frehiwot", "Mengistu"),
                ("Kassa", "Mekuria"),
                ("Yemisrach", "Haile"),
                ("Taye", "Bekri"),
                ("Nardos", "Shimelis"),
                ("Getahun", "Assefa"),
                ("Seble", "Yonas"),
                ("Tesfaye", "Amanuel"),
                ("Almaz", "Gebremedhin"),
                ("Soliana", "Berhanu"),
                ("Hailu", "Mekasha"),
                ("Genet", "Yimer"),
                ("Teodros", "Yirga"),
                ("Senait", "Gebremichael"),
                ("Eshetu", "Abebe"),
                ("Hiwot", "Tekle"),
                ("Tesfanesh", "Feyssa"),
                ("Dagim", "Belete"),
                ("Winta", "Girmay"),
                ("Zerihun", "Asmare"),
                ("Amsalu", "Negash"),
            ]
        )
    ]

    demo_teacher_users = [
        User(
            username=f"teacher{i}",
            password="Password#123",
            first_name=first,
            last_name=last,
            date_of_birth=datetime.date(
                1990 + i % 10, (i % 12) + 1, (i % 28) + 1
            ),
            email=f"{first.lower()}.{last.lower()}@example.com",
            phone_number=f"+251911000{i:02d}",
            is_active=True,
        )
        for i, (first, last) in enumerate(
            [
                ("Abraham", "Mulugeta"),
                ("Saba", "Gizachew"),
                ("Gashaw", "Haile"),
                ("Mulu", "Tesfahun"),
                ("Yordanos", "Getnet"),
                ("Asnakech", "Taddesse"),
                ("Brook", "Kassahun"),
                ("Yeshiwas", "Aberra"),
                ("Wondimu", "Tesfaye"),
                ("Martha", "Worku"),
            ]
        )
    ]

    demo_staff_users = [
        User(
            username=f"staff{i}",
            password="Password#123",
            first_name=first,
            last_name=last,
            date_of_birth=datetime.date(
                1990 + i % 10, (i % 12) + 1, (i % 28) + 1
            ),
            email=f"{first.lower()}.{last.lower()}@example.com",
            phone_number=f"+251911000{i:02d}",
            is_active=True,
        )
        for i, (first, last) in enumerate(
            [
                ("Tigist", "Alemayehu"),
                ("Mesfin", "Abebe"),
                ("Selamawit", "Gebru"),
                ("Fitsum", "Bekele"),
                ("Rediet", "Hagos"),
            ]
        )
    ]

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


def seed_demo_batches():
    """Create fresh batches for demo"""

    # Create demo batches
    print("Creating batches")
    print("----------------------")

    demo_batches = [
        Batch(
            name="Grade7_2015EC", level=7, start_date=datetime.date(2015, 9, 1)
        ),
        Batch(
            name="Grade8_2014EC", level=8, start_date=datetime.date(2014, 9, 1)
        ),
        Batch(
            name="Grade9_2013EC", level=9, start_date=datetime.date(2013, 9, 1)
        ),
        Batch(
            name="Grade10_2012EC",
            level=10,
            start_date=datetime.date(2012, 9, 1),
        ),
    ]

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


def seed_demo_student_profiles():
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
        user.student_profile.batch = batches_list[i % demo_batches_len]
        user.student_profile.save()

    # Check that it worked
    print("Student Profiles Created:")
    for student in student_users:
        print(
            f"Student: {student.username} - {student.first_name} {student.last_name} - {student.student_profile.batch.name}"
        )
    print("------------------------")


def seed_demo_teacher_profiles():
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


def seed_demo_staff_profiles():
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


def seed_departments_and_subjects():
    """Creates departments and subjects"""

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

    print("Creating subjects")
    print("----------------------")
    # Fetch (including existing) for foreign-key mapping
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
    seed_demo_roles()
    seed_demo_users()
    assign_demo_roles()
    seed_demo_batches()
    seed_demo_student_profiles()
    seed_demo_teacher_profiles()
    seed_demo_staff_profiles()
    assign_user_addresses()
    seed_departments_and_subjects()

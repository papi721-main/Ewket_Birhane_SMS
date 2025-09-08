#!/usr/bin/env python3

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

from core.models import (
    Batch,
    Role,
    Staff_Profile,
    Student_Profile,
    Teacher_Profile,
    User,
)

demo_roles = [
    Role(pk=1, name="Student", description="A student in the school"),
    Role(pk=2, name="Teacher", description="A teacher in the school"),
    Role(
        pk=3,
        name="Staff",
        description="A member of the school serving as a staff",
    ),
]

demo_student_users = [
    User(
        username=f"student{i}",
        password="Password#123",
        first_name=first,
        last_name=last,
        date_of_birth=datetime.date(1990 + i % 10, (i % 12) + 1, (i % 28) + 1),
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
        date_of_birth=datetime.date(1990 + i % 10, (i % 12) + 1, (i % 28) + 1),
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
        date_of_birth=datetime.date(1990 + i % 10, (i % 12) + 1, (i % 28) + 1),
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

demo_batches = [
    Batch(name="Grade7_2015EC", level=7, start_date=datetime.date(2015, 9, 1)),
    Batch(name="Grade8_2014EC", level=8, start_date=datetime.date(2014, 9, 1)),
    Batch(name="Grade9_2013EC", level=9, start_date=datetime.date(2013, 9, 1)),
    Batch(
        name="Grade10_2012EC", level=10, start_date=datetime.date(2012, 9, 1)
    ),
]

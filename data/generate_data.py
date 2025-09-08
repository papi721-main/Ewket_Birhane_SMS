#!/usr/bin/env python3
"""generate_data.py

This is a script for generating data using Django ORM

"""

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

# 3. Now you can safely import your models
from core.models import Role, User  # noqa - ignore pycodestyle

# ---


def create_demo_roles():
    """Removes all previous roles and create fresh roles for a demo"""

    roles = Role.objects.all()
    roles.delete()

    Role.objects.bulk_create(
        [
            Role(pk=1, name="Student", description="A student in the school"),
            Role(pk=2, name="Teacher", description="A teacher in the school"),
            Role(
                pk=3,
                name="Assistant",
                description="A member of the school serving as an assistant for a batch",
            ),
            Role(
                pk=4,
                name="Coordinator",
                description="A member of the school serving as a coordinator",
            ),
            Role(
                pk=5,
                name="Head",
                description="A member of the school serving as the head of the school",
            ),
        ]
    )

    # Check that it worked
    roles = Role.objects.all()
    print("Roles Created:")
    print("---------------")
    for role in roles:
        print(f"Role: {role.name} - {role.description}")
    print("---------------")


if __name__ == "__main__":
    create_demo_roles()

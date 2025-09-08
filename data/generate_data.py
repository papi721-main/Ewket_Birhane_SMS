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

# 1. Tell Django where your settings module is
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "main.settings"
)  # adjust to your project

# 2. Setup Django
django.setup()

# 3. Now you can safely import your models
from core.models import Role, User  # noqa

papi721 = User.objects.get(username="papi721")
print(papi721)

#!/usr/bin/env python3

from django.db import models


class User(models.Model):
    """Model representing a user in the system."""

    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)  # pyright: ignore
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class User_Address(models.Model):
    """Model representing an address for a user."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True
    )  # If a user is deleted, the corresponding address is deleted
    street_address = models.CharField(max_length=255)
    woreda = models.IntegerField()
    sub_city = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Emergency_Contact(models.Model):
    """Model representing an emergency contact for a user."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # if a user is deleted, the corresponding emergency contact is deleted
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Emergency_Contact_Address(models.Model):
    """Model representing an address for an emergency contact."""

    emergency_contact = models.ForeignKey(
        Emergency_Contact, on_delete=models.CASCADE, null=True
    )  # If an emergency contact is deleted, the corresponding address is deleted
    street_address = models.CharField(max_length=255)
    woreda = models.IntegerField()
    sub_city = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Role(models.Model):
    """Model representing a role in the system."""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(
        User, through="User_Role", related_name="roles"
    )


class User_Role(models.Model):
    """Model representing a user-role relationship."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # If a user is deleted, the user-role relationship is deleted
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE
    )  # If a role is deleted, the user-role relationship is deleted
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "role"],
                name="uniq_user_role",
                # User-role relationship must be unqiue per (user, role)
                # This is to avoid assigning the same role to the same user multiple times
            ),
        ]


class Batch(models.Model):
    """Model representing the batch for students."""

    name = models.CharField(max_length=100, unique=True, blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(null=True)
    level = models.IntegerField()
    description = models.TextField(blank=True)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Student_Profile(models.Model):
    """Model representing a student profile."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True
    )  # If a user is deleted, the student profile is deleted
    batch = models.ForeignKey(
        Batch, on_delete=models.SET_NULL, null=True
    )  # If a batch is deleted, the student profile is set to null
    joined_at = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Teacher_Profile(models.Model):
    """Model representing a teacher profile."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True
    )  # If a user is deleted, the teacher profile is deleted
    start_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Staff_Profile(models.Model):
    """Model representing a staff profile."""

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True
    )  # If a user is deleted, the staff profile is deleted
    start_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Department(models.Model):
    """Model representing a department."""

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Subject(models.Model):
    """Model representing a subject."""

    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True
    )  # If a department is deleted, department field will be null for the subject
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    """Model representing a course.

    Description:
        - This model is used to keep track of the courses offered to a batch in a specific year/semester
    """

    subject = models.ForeignKey(
        Subject, on_delete=models.SET_NULL, null=True
    )  # If a subject is deleted, subject field will be null for the course
    teacher = models.ForeignKey(
        Teacher_Profile, on_delete=models.SET_NULL, null=True
    )  # If a teacher is deleted, teacher field will be null for the course
    batch = models.ForeignKey(
        Batch, on_delete=models.SET_NULL, null=True
    )  # If a batch is deleted, batch field will be null for the course
    staff = models.ForeignKey(
        Staff_Profile, on_delete=models.SET_NULL, null=True
    )  # If a staff is deleted, staff field will be null for the course

    description = models.TextField(blank=True)
    semester = models.IntegerField()
    year = models.IntegerField()
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["subject", "batch", "semester", "year"],
                name="uniq_subject_batch_semester_year",
                # Course must be unqiue per (subject, batch, semester, year)
                # This is to avoid offering the same course multiple times in the same batch for the same semester and year
            )
        ]


class Enrollment(models.Model):
    """Model representing an enrollment."""

    student = models.ForeignKey(
        Student_Profile, on_delete=models.CASCADE
    )  # If a student is deleted, the enrollment record is deleted as well

    course = models.ForeignKey(
        Course, on_delete=models.CASCADE
    )  # If a course is deleted, the enrollment record is deleted as well
    enrollment_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True)
    grade = models.CharField(max_length=2, blank=True)
    rank = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "course"],
                name="uniq_student_course",
                # Enrollment must be unqiue per (student, course)
                # This is to avoid enrolling the same student in the same course multiple times
            )
        ]


class Assessment(models.Model):
    """Model representing assessments taken by a student in an enrollment."""

    enrollment = models.ForeignKey(
        Enrollment, on_delete=models.CASCADE
    )  # If an enrollment is deleted, the assessment records are deleted as well
    type = models.CharField(max_length=100)
    score = models.FloatField(null=True)
    total_score = models.FloatField(null=True)
    given_at = models.DateTimeField(blank=True, null=True)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

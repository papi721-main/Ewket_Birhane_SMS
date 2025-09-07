#!/usr/bin/env python3

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model extending Django's AbstractUser.
    Purpose: Represents all users in the system, including authentication and profile information.
    Stores personal details and is the central entity for user-related relationships.
    """

    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User: {self.username}, {self.first_name} {self.last_name}, {self.email}, {self.phone_number}"


class User_Address(models.Model):
    """
    Stores address information for a user.
    Purpose: Allows each user to have one or more physical addresses associated with their account.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )  # If a user is deleted, the corresponding address is deleted
    street_address = models.CharField(max_length=255)
    woreda = models.IntegerField()
    sub_city = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"User_Address: {self.user}, {self.street_address}, {self.city}, {self.country}"


class Emergency_Contact(models.Model):
    """
    Stores emergency contact information for a user.
    Purpose: Enables users to register people to be contacted in case of emergency, with their relationship and contact details.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )  # if a user is deleted, the corresponding emergency contact is deleted
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Emergency_Contact: {self.first_name} {self.last_name}, {self.relationship}, {self.user}"


class Emergency_Contact_Address(models.Model):
    """
    Stores address information for an emergency contact.
    Purpose: Allows each emergency contact to have one or more physical addresses.
    """

    emergency_contact = models.ForeignKey(
        Emergency_Contact, on_delete=models.CASCADE
    )  # If an emergency contact is deleted, the corresponding address is deleted
    street_address = models.CharField(max_length=255)
    woreda = models.IntegerField()
    sub_city = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Emergency_Contact_Address: {self.emergency_contact}, {self.street_address}, {self.city}, {self.country}"


class Role(models.Model):
    """
    Represents a role that can be assigned to users (e.g., student, teacher, staff).
    Purpose: Supports role-based access and permissions by associating users with specific roles.
    """

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, through="User_Role", related_name="roles"
    )

    def __str__(self):
        return f"Role: {self.name}"


class User_Role(models.Model):
    """
    Junction table for the many-to-many relationship between users and roles.
    Purpose: Tracks which users have which roles, and enforces uniqueness for each user-role pair.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
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

    def __str__(self):
        return f"User_Role: {self.user}, {self.role}, {self.user.first_name} {self.user.last_name}"  # pyright:ignore


class Batch(models.Model):
    """
    Represents a batch or cohort of students.
    Purpose: Groups students by academic year, level, or intake for organizational and reporting purposes.
    """

    name = models.CharField(max_length=100, unique=True, blank=False)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(null=True)
    level = models.IntegerField()
    description = models.TextField(blank=True)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Batch: {self.name}, Level {self.level}, {self.start_date}"


class Student_Profile(models.Model):
    """
    Profile model for student users.
    Purpose: Stores student-specific information and links each student to a batch.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )  # If a user is deleted, the student profile is deleted
    batch = models.ForeignKey(
        Batch, on_delete=models.SET_NULL, null=True
    )  # If a batch is deleted, the student profile is set to null
    joined_at = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Student_Profile: {self.user}, {self.batch}, Joined: {self.joined_at}"


class Teacher_Profile(models.Model):
    """
    Profile model for teacher users.
    Purpose: Stores teacher-specific information, such as employment start date and remarks.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )  # If a user is deleted, the teacher profile is deleted
    start_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Teacher_Profile: {self.user}, Start: {self.start_date}"


class Staff_Profile(models.Model):
    """
    Profile model for staff users.
    Purpose: Stores staff-specific information, such as employment start date and remarks.
    """

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )  # If a user is deleted, the staff profile is deleted
    start_date = models.DateField(null=True, blank=True)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Staff_Profile: {self.user}, Start: {self.start_date}"


class Department(models.Model):
    """
    Represents an academic or administrative department within the institution.
    Purpose: Organizes subjects and courses under specific departments.
    """

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Department: {self.name}"


class Subject(models.Model):
    """
    Represents an academic subject offered by a department.
    Purpose: Defines the subjects that can be taught and linked to courses.
    """

    department = models.ForeignKey(
        Department, on_delete=models.SET_NULL, null=True
    )  # If a department is deleted, department field will be null for the subject
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Subject: {self.name}, Department: {self.department}"


class Course(models.Model):
    """
    Represents a course offering for a specific batch, subject, teacher, and semester/year.
    Purpose: Tracks which courses are available to which batches, who teaches them, and in which academic period.
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

    def __str__(self):
        return f"Course: {self.subject}, {self.batch}, Semester: {self.semester}, Year: {self.year}"


class Enrollment(models.Model):
    """
    Represents a student's enrollment in a specific course.
    Purpose: Tracks which students are enrolled in which courses, including enrollment status and grades.
    """

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

    def __str__(self):
        return (
            f"Enrollment: {self.student}, {self.course}, Grade: {self.grade}"
        )


class Assessment(models.Model):
    """
    Represents an assessment or exam taken by a student as part of a course enrollment.
    Purpose: Records assessment type, scores, and related details for each enrollment.
    """

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

    def __str__(self):
        return f"Assessment: {self.type}, {self.enrollment}, Score: {self.score}/{self.total_score}"

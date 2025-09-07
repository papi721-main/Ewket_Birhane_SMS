# Core App Data Model Documentation

This document provides an overview of the models in the `core` app and their relationships.

---

## User

- **Inherits:** `AbstractUser`
- **Fields:**
  - `first_name` (CharField, max_length=100)
  - `last_name` (CharField, max_length=100)
  - `date_of_birth` (DateField)
  - `age` (IntegerField, nullable)
  - `email` (EmailField, unique)
  - `phone_number` (CharField, max_length=15, unique)
  - `created_at` (DateTimeField, auto_now_add)
  - `modified_at` (DateTimeField, auto_now)
- **Relationships:**
  - One-to-many with `User_Address`, `Emergency_Contact`
  - Many-to-many with `Role` (through `User_Role`)
  - One-to-one with `Student_Profile`, `Teacher_Profile`, `Staff_Profile`

---

## User_Address

- **Purpose:** Stores addresses for users.
- **Fields:**
  - `user` (ForeignKey to User, nullable, CASCADE)
  - `street_address`, `woreda`, `sub_city`, `city`, `country`
  - `created_at`, `modified_at`

---

## Emergency_Contact

- **Purpose:** Emergency contacts for users.
- **Fields:**
  - `user` (ForeignKey to User, CASCADE)
  - `first_name`, `last_name`, `relationship`, `phone_number` (unique), `email`
  - `created_at`, `modified_at`
- **Relationships:**
  - One-to-many with `Emergency_Contact_Address`

---

## Emergency_Contact_Address

- **Purpose:** Address for an emergency contact.
- **Fields:**
  - `emergency_contact` (ForeignKey to Emergency_Contact, nullable, CASCADE)
  - `street_address`, `woreda`, `sub_city`, `city`, `country`
  - `created_at`, `modified_at`

---

## Role

- **Purpose:** Represents a user role (e.g., student, teacher, staff).
- **Fields:**
  - `name` (unique), `description`, `created_at`, `modified_at`
- **Relationships:**
  - Many-to-many with `User` (through `User_Role`)

---

## User_Role

- **Purpose:** Junction table for user-role relationships.
- **Fields:**
  - `user` (ForeignKey to User, CASCADE)
  - `role` (ForeignKey to Role, CASCADE)
  - `created_at`, `modified_at`
- **Constraints:**
  - Unique together: (`user`, `role`)

---

## Batch

- **Purpose:** Represents a student batch.
- **Fields:**
  - `name` (unique), `start_date`, `end_date`, `level`, `description`, `remarks`, `created_at`, `modified_at`

---

## Student_Profile

- **Purpose:** Profile for student users.
- **Fields:**
  - `user` (OneToOneField to User, primary_key, CASCADE)
  - `batch` (ForeignKey to Batch, SET_NULL)
  - `joined_at`, `created_at`, `modified_at`

---

## Teacher_Profile

- **Purpose:** Profile for teacher users.
- **Fields:**
  - `user` (OneToOneField to User, primary_key, CASCADE)
  - `start_date`, `remarks`, `created_at`, `modified_at`

---

## Staff_Profile

- **Purpose:** Profile for staff users.
- **Fields:**
  - `user` (OneToOneField to User, primary_key, CASCADE)
  - `start_date`, `remarks`, `created_at`, `modified_at`

---

## Department

- **Purpose:** Academic departments.
- **Fields:**
  - `name` (unique), `description`, `created_at`, `modified_at`

---

## Subject

- **Purpose:** Academic subjects.
- **Fields:**
  - `department` (ForeignKey to Department, SET_NULL)
  - `name` (unique), `description`, `created_at`, `modified_at`

---

## Course

- **Purpose:** Courses offered to batches in a specific year/semester.
- **Fields:**
  - `subject` (ForeignKey to Subject, SET_NULL)
  - `teacher` (ForeignKey to Teacher_Profile, SET_NULL)
  - `batch` (ForeignKey to Batch, SET_NULL)
  - `staff` (ForeignKey to Staff_Profile, SET_NULL)
  - `description`, `semester`, `year`, `remarks`, `created_at`, `modified_at`
- **Constraints:**
  - Unique together: (`subject`, `batch`, `semester`, `year`)

---

## Enrollment

- **Purpose:** Student enrollment in courses.
- **Fields:**
  - `student` (ForeignKey to Student_Profile, CASCADE)
  - `course` (ForeignKey to Course, CASCADE)
  - `enrollment_date`, `status`, `grade`, `rank`, `created_at`, `modified_at`
- **Constraints:**
  - Unique together: (`student`, `course`)

---

## Assessment

- **Purpose:** Assessments for student enrollments.
- **Fields:**
  - `enrollment` (ForeignKey to Enrollment, CASCADE)
  - `type`, `score`, `total_score`, `given_at`, `remarks`, `created_at`, `modified_at`

---

## Relationships Summary Table

| Model                | Related Model(s)         | Relationship Type         |
|----------------------|-------------------------|--------------------------|
| User                 | User_Address            | One-to-Many              |
| User                 | Emergency_Contact       | One-to-Many              |
| User                 | Role                    | Many-to-Many (User_Role) |
| User                 | Student/Teacher/Staff   | One-to-One (Profile)     |
| Student_Profile      | Batch                   | Many-to-One              |
| Teacher_Profile      | -                       | -                        |
| Staff_Profile        | -                       | -                        |
| Emergency_Contact    | Emergency_Contact_Address| One-to-Many             |
| Role                 | User                    | Many-to-Many (User_Role) |
| Course               | Subject, Teacher, Batch, Staff | Many-to-One      |
| Enrollment           | Student_Profile, Course | Many-to-One              |
| Assessment           | Enrollment              | Many-to-One              |

---

For a visual representation, see the ERD in `docs/ERD_v7_Final.png`.

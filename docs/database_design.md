# 📘 Database Documentation

This document describes the database schema of the **Ewket Birhane Student Management System**, based on the finalized ERD. The system supports user management, academic structuring, student enrollment, course offerings, and performance tracking.

Here is the ERD diagram for reference:

![ERD Diagram](./ERD5-final.png)

---

## 🧑‍💻 User and Role Management

### `User`

Stores authentication and general identity information for all system users.

| Field          | Type         | Constraints                 |
| -------------- | ------------ | --------------------------- |
| `user_id`      | INTEGER      | PK, Auto-increment          |
| `username`     | VARCHAR(50)  | UNIQUE, NOT NULL            |
| `password`     | TEXT         | NOT NULL                    |
| `first_name`   | VARCHAR(50)  | NOT NULL                    |
| `last_name`    | VARCHAR(50)  | NOT NULL                    |
| `email`        | VARCHAR(100) | NULLABLE                    |
| `phone_number` | VARCHAR(20)  | NULLABLE                    |
| `address`      | TEXT         | NULLABLE                    |
| `is_active`    | BOOLEAN      | DEFAULT TRUE                |
| `created_at`   | DATETIME     | DEFAULT CURRENT_TIMESTAMP   |
| `modified_at`  | DATETIME     | ON UPDATE CURRENT_TIMESTAMP |

---
### `Role`

Defines user roles in the system.

| Field       | Type         | Constraints               |
|-------------|--------------|----------------------------|
| `role_id`   | INTEGER      | PK, Auto-increment         |
| `name`      | VARCHAR(30)  | UNIQUE, NOT NULL           |
| `description`| TEXT        | NULLABLE                   |

---
### `User_Role`

Associative entity that maps users to roles (many-to-many relationship).

| Field         | Type      | Constraints                   |
|---------------|-----------|-------------------------------|
| `user_role_id`| INTEGER   | PK, Auto-increment            |
| `user_id`     | INTEGER   | FK → User(user_id), NOT NULL |
| `role_id`     | INTEGER   | FK → Role(role_id), NOT NULL |

---
## 🧑‍🎓 User Profiles

### `Student_Profile`

Stores extended student-specific data.

| Field                    | Type        | Constraints                        |
|--------------------------|-------------|-------------------------------------|
| `student_id`             | INTEGER     | PK, FK → User(user_id)             |
| `batch_id`               | INTEGER     | FK → Batch(batch_id)               |
| `date_of_birth`          | DATE        | NOT NULL                           |
| `emergency_contact_name` | VARCHAR(100)| NOT NULL                           |
| `emergency_contact_phone`| VARCHAR(20) | NOT NULL                           |
| `emergency_contact_address` | TEXT    | NULLABLE                           |
| `joined_at`              | DATE        | DEFAULT CURRENT_DATE               |

---
### `Teacher_Profile`

Stores extended teacher-specific data.

| Field        | Type    | Constraints            |
| ------------ | ------- | ---------------------- |
| `teacher_id` | INTEGER | PK, FK → User(user_id) |
| `start_date` | DATE    | NOT NULL               |
| `remark`     | TEXT    | NULLABLE               |

---
### `Staff_Profile`

Stores extended staff-specific data (Admin, Coordinator, etc.).

| Field         | Type      | Constraints                     |
|---------------|-----------|----------------------------------|
| `staff_id`    | INTEGER   | PK, FK → User(user_id)          |
| `start_date`  | DATE      | NOT NULL                        |
| `remark`      | TEXT      | NULLABLE                        |

---
## 🎓 Academic Structuring

### `Batch`

Groups students into cohorts (e.g. Grade7_2024).

| Field       | Type        | Constraints                    |
|-------------|-------------|---------------------------------|
| `batch_id`  | INTEGER     | PK, Auto-increment             |
| `name`      | VARCHAR(50) | UNIQUE, NOT NULL               |
| `start_date`| DATE        | NOT NULL                       |
| `end_date`  | DATE        | NULLABLE                       |
| `level`     | INTEGER     | NOT NULL                       |
| `description`| TEXT       | NULLABLE                       |
| `remark`    | TEXT        | NULLABLE                       |

---
### `Department`

Defines academic departments (e.g. Theology, Mezmur).

| Field           | Type          | Constraints             |
|------------------|---------------|--------------------------|
| `department_id`  | INTEGER       | PK, Auto-increment       |
| `name`           | VARCHAR(50)   | UNIQUE, NOT NULL         |
| `description`    | TEXT          | NULLABLE                 |

---
### `Subject`

Defines subjects taught in the system.

| Field        | Type          | Constraints                        |
|--------------|---------------|-------------------------------------|
| `subject_id` | INTEGER       | PK, Auto-increment                 |
| `class_id`   | INTEGER       | FK → Department(department_id)     |
| `name`       | VARCHAR(50)   | NOT NULL                           |
| `description`| TEXT          | NULLABLE                           |

---
## 📚 Course & Enrollment

### `Course`

Represents a subject offered to a batch in a specific year/semester.

| Field        | Type          | Constraints                                         |
|--------------|---------------|-----------------------------------------------------|
| `course_id`  | INTEGER       | PK, Auto-increment                                  |
| `subject_id` | INTEGER       | FK → Subject(subject_id), NOT NULL                 |
| `teacher_id` | INTEGER       | FK → Teacher_Profile(teacher_id), NOT NULL         |
| `batch_id`   | INTEGER       | FK → Batch(batch_id), NOT NULL                     |
| `name`       | VARCHAR(100)  | NOT NULL                                           |
| `description`| TEXT          | NULLABLE                                           |
| `semester`   | INTEGER       | CHECK (semester IN (1, 2)), NOT NULL               |
| `year`       | INTEGER       | NOT NULL                                           |
| `remarks`    | TEXT          | NULLABLE                                           |
| `created_at` | DATETIME      | DEFAULT CURRENT_TIMESTAMP                          |
| `modified_at`| DATETIME      | ON UPDATE CURRENT_TIMESTAMP                        |

📌 **Constraint:** Unique on (`subject_id`, `teacher_id`, `batch_id`, `semester`, `year`)

---
### `Enrollment`

Tracks student enrollment information in a course.

| Field           | Type      | Constraints                             |
|------------------|-----------|------------------------------------------|
| `enrollment_id`  | INTEGER   | PK, Auto-increment                      |
| `student_id`     | INTEGER   | FK → Student_Profile(student_id)        |
| `course_id`      | INTEGER   | FK → Course(course_id)                  |
| `enrollment_date`| DATE      | DEFAULT CURRENT_DATE                    |
| `status`         | VARCHAR(20) | CHECK (status IN ('Active','Completed','Dropped')) |
| `grade`          | FLOAT     | NULLABLE                                |
| `rank`           | INTEGER   | NULLABLE                                |
| `remark`         | TEXT      | NULLABLE                                |
| `created_at`     | DATETIME  | DEFAULT CURRENT_TIMESTAMP               |
| `modified_at`    | DATETIME  | ON UPDATE CURRENT_TIMESTAMP             |

📌 **Constraint:** Unique on (`student_id`, `course_id`)

---

## 📝 Assessment

### `Assessment`

Stores individual scores for a student's course performance.

| Field         | Type        | Constraints                       |
|---------------|-------------|------------------------------------|
| `assessment_id`| INTEGER     | PK, Auto-increment                |
| `enrollment_id`| INTEGER     | FK → Enrollment(enrollment_id)   |
| `type`        | VARCHAR(30) | e.g., quiz, mid, final, etc.      |
| `score`       | FLOAT       | NOT NULL                          |
| `total_score` | FLOAT       | NOT NULL                          |
| `given_at`    | DATE        | NOT NULL                          |
| `created_at`  | DATETIME    | DEFAULT CURRENT_TIMESTAMP         |
| `modified_at` | DATETIME    | ON UPDATE CURRENT_TIMESTAMP       |
| `remarks`     | TEXT        | NULLABLE                          |

---
## 🔗 Relationships Summary

- `User` connects 1:1 with `Student_Profile`, `Teacher_Profile`, or `Staff_Profile`
- `User` connects M:N with `Role` through `User_Role`
- `Student_Profile` links to `Batch`
- `Subject` links to `Department`
- `Course` links to `Subject`, `Teacher_Profile`, `Batch`
- `Enrollment` links students to courses
- `Assessment` links to enrollments (multiple per enrollment)

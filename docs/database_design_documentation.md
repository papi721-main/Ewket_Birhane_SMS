  📚 Database Schema for Student Management System

This document describes the database schema of the **Ewket Birhane Student Management System**, based on the finalized ERD diagram. The system supports user management, academic structuring, student enrollment, and course offerings, and performance tracking.

Here is the final ERD diagram:

![ERD Diagram](./ERD_v7_Final.png)

---

## 🧑‍ User Management

### Table: `User`

Stores account information for all system users (students, teachers, staff, admins).

| Field           | Data Type | Constraints                  | Description                                    |
| --------------- | --------- | ---------------------------- | ---------------------------------------------- |
| `user_id`       | Integer   | PK, Auto-increment           | Unique identifier for the user                 |
| `username`      | Text      | UNIQUE, NOT NULL             | Login name for the user                        |
| `password`      | Text      | NOT NULL                     | Hashed password                                |
| `first_name`    | Text      | NOT NULL                     | First name of the user                         |
| `last_name`     | Text      | NOT NULL                     | Last name of the user                          |
| `date_of_birth` | DATE      | NOT NULL                     | Date of birth                                  |
| `email`         | Text      |              | User email address                             |
| `phone_number`  | Text      | NOT NULL                     | User phone number                              |
| `is_active`     | Boolean   | Default: true                | Boolean to indicate whether the user is active |
| `created_at`      | DATETIME    | DEFAULT CURRENT_TIMESTAMP                          | Timestamp                                                   |
| `modified_at`     | DATETIME    | ON UPDATE CURRENT_TIMESTAMP                        | Timestamp                                                   |

---

### Table: `User_Address`

Stores address data in a query-able structure (Ethiopian context).

| Field         | Data Type | Constraints                                    | Description    |
| ------------- | --------- | ---------------------------------------------- | -------------- |
| `address_id`  | Integer   | PK, Auto-increment                             | Unique ID      |
| `user_id`     | Integer   | FK → User(user_id)                   | Linked user    |
| `street_name` | Text      | NOT NULL                                  | Street name    |
| `woreda`      | Integer   | NOT NULL                                       | Woreda         |
| `sub_city`    | Text      | NOT NULL                                       | Sub-city       |
| `city`        | Text      | NOT NULL                                       | City           |
| `country`     | Text      | Default: 'Ethiopia'                            | Country        |

---

### Table: `Emergency_Contact`

Stores emergency contact info for users.

| Field          | Data Type | Constraints                  | Description                     |
| -------------- | --------- | ---------------------------- | ------------------------------- |
| `contact_id`   | Integer   | PK, Auto-increment           | Unique ID                       |
| `user_id`      | Integer   | FK → User(user_id), NOT NULL | The user the contact belongs to |
| `first_name`   | Text      | NOT NULL                     | First name of contact           |
| `last_name`    | Text      | NOT NULL                     | Last name of contact            |
| `email`        | Text      |                              | Contact email                   |
| `relationship` | Text      |       | Relationship to the user        |
| `phone_number` | Text      | NOT NULL                     | Phone number                    |
| `created_at`      | DATETIME    | DEFAULT CURRENT_TIMESTAMP                          | Timestamp                                                   |
| `modified_at`     | DATETIME    | ON UPDATE CURRENT_TIMESTAMP                        | Timestamp                                                   |

---

### Table: `Emergency_Contact_Address`

Stores address data in a query-able structure (Ethiopian context).

| Field         | Data Type | Constraints                                    | Description    |
| ------------- | --------- | ---------------------------------------------- | -------------- |
| `address_id`  | Integer   | PK, Auto-increment                             | Unique ID      |
| `contact_id`  | Integer   | FK → Emergency_Contact(`contact_id`) | Linked contact |
| `street_name` | Text      | NOT NULL                                  | Street name    |
| `woreda`      | Integer   | NOT NULL                                       | Woreda         |
| `sub_city`    | Text      | NOT NULL                                       | Sub-city       |
| `city`        | Text      | NOT NULL                                       | City           |
| `country`     | Text      | Default: 'Ethiopia'                            | Country        |

---

### Table: `Role`

Defines access roles.

| Field         | Data Type | Constraints                   | Description                                                 |
| ------------- | --------- | ----------------------------- | ----------------------------------------------------------- |
| `role_id`     | Integer   | PK, Auto-increment            | Unique ID for the role                                      |
| `name`        | Text      | UNIQUE (Student, Admin, etc.) | Name of the role (e.g., Student, Teacher, Assistant, Admin) |
| `description` | Text      |                               | Description of the role                                     |
| `created_at`      | DATETIME    | DEFAULT CURRENT_TIMESTAMP                          | Timestamp                                                   |
| `modified_at`     | DATETIME    | ON UPDATE CURRENT_TIMESTAMP                        | Timestamp                                                   |

---

### Table: `User_Role`

Associative entity that maps users to roles (many-to-many relationship).

| Field          | Data Type | Constraints        | Description         |
| -------------- | --------- | ------------------ | ------------------- |
| `user_role_id` | Integer   | PK, Auto-increment | Unique identifier   |
| `user_id`      | Integer   | FK → User          | The associated user |
| `role_id`      | Integer   | FK → Role          | The associated role |
| `created_at`      | DATETIME    | DEFAULT CURRENT_TIMESTAMP                          | Timestamp                                                   |
| `modified_at`     | DATETIME    | ON UPDATE CURRENT_TIMESTAMP                        | Timestamp                                                   |

---

## 👨‍🏫  User Profiles

### Table: `Student_Profile`

Stores extended student-specific data.

| Field        | Type    | Constraints            | Description                            |
| ------------ | ------- | ---------------------- | -------------------------------------- |
| `student_id` | INTEGER | PK, FK → User(user_id) | Same as user_id, acts as PK and FK     |
| `batch_id`   | INTEGER | FK → Batch(batch_id), NULLABLE   | The batch to which the student belongs |
| `joined_at`  | DATE    |                | Date the student joined                |
| `created_at`      | DATETIME    | DEFAULT CURRENT_TIMESTAMP                          | Timestamp                                                   |
| `modified_at`     | DATETIME    | ON UPDATE CURRENT_TIMESTAMP                        | Timestamp                                                   |

---

### Table: `Teacher_Profile`

Stores extended teacher-specific data.

| Field        | Type    | Constraints            | Description                        |
| ------------ | ------- | ---------------------- | ---------------------------------- |
| `teacher_id` | INTEGER | PK, FK → User(user_id) | Same as user_id, acts as PK and FK |
| `start_date` | DATE    |                | Start date of teaching             |
| `remark`     | TEXT    |                | Additional notes                   |
| `created_at`      | DATETIME    | DEFAULT CURRENT_TIMESTAMP                          | Timestamp                                                   |
| `modified_at`     | DATETIME    | ON UPDATE CURRENT_TIMESTAMP                        | Timestamp                                                   |

---

### Table: `Staff_Profile`

Stores extended staff-specific data (Admin, Coordinator, etc.).

| Field        | Type    | Constraints            | Description                        |
| ------------ | ------- | ---------------------- | ---------------------------------- |
| `staff_id`   | INTEGER | PK, FK → User(user_id) | Same as user_id, acts as PK and FK |
| `start_date` | DATE    |                | Start date of staff                |
| `remark`     | TEXT    |                | Additional notes                   |
| `created_at`      | DATETIME    | DEFAULT CURRENT_TIMESTAMP                          | Timestamp                                                   |
| `modified_at`     | DATETIME    | ON UPDATE CURRENT_TIMESTAMP                        | Timestamp                                                   |

---

## 🎓 Academic Structuring

### Table: `Batch`

Groups students into cohorts (e.g. `Grade7_2024`).

| Field         | Type        | Constraints      | Description                                                         |
| ------------- | ----------- | ---------------- | ------------------------------------------------------------------- |
| `batch_id`    | INTEGER     | PK               | Unique identifier                                                   |
| `name`        | VARCHAR(50) | UNIQUE, NOT NULL | Computed name from grade level and start year (e.g., `Grade7_2024`) |
| `start_date`  | DATE        | NOT NULL         | Date when batch started                                             |
| `end_date`    | DATE        |          | Optional date when the batch ended enrollment                       |
| `level`       | INTEGER     | NOT NULL         | Grade level (e.g., 7, 8, 9)                                         |
| `description` | TEXT        |          | Details about the batch                                             |
| `remark`      | TEXT        |          | Extra notes on the batch                                            |
| `created_at`      | DATETIME    | DEFAULT CURRENT_TIMESTAMP                          | Timestamp                                                   |
| `modified_at`     | DATETIME    | ON UPDATE CURRENT_TIMESTAMP                        | Timestamp                                                   |

---

### Table: `Department`

Defines academic departments (e.g. Theology, Mezmur).

| Field           | Type        | Constraints      | Description            |
| --------------- | ----------- | ---------------- | ---------------------- |
| `department_id` | INTEGER     | PK               | Unique identifier      |
| `name`          | VARCHAR(50) | UNIQUE, NOT NULL | Name of the department |
| `description`   | TEXT        |          | Department description |
| `created_at`      | DATETIME    | DEFAULT CURRENT_TIMESTAMP                          | Timestamp                                                   |
| `modified_at`     | DATETIME    | ON UPDATE CURRENT_TIMESTAMP                        | Timestamp                                                   |

---

### Table: `Subject`

Defines subjects taught in the system.

| Field           | Type        | Constraints                      | Description                                     |
| --------------- | ----------- | -------------------------------- | ----------------------------------------------- |
| `subject_id`    | INTEGER     | PK, Auto-increment               | Unique identifier                               |
| `department_id` | INTEGER     | FK → Department(`department_id`), NULLABLE | The department the course belongs to            |
| `name`          | VARCHAR(50) | NOT NULL                         | Name of the subject (e.g., Bible Study, Mezmur) |
| `description`   | TEXT        |                          | Description on the subject                      |
| `created_at`      | DATETIME    | DEFAULT CURRENT_TIMESTAMP                          | Timestamp                                                   |
| `modified_at`     | DATETIME    | ON UPDATE CURRENT_TIMESTAMP                        | Timestamp                                                   |

---

## 📚 Course & Enrollment

### Table: `Course`

Represents a subject offered to a batch in a specific year/semester.

| Field         | Type     | Constraints                                  | Description                         |
| ------------- | -------- | -------------------------------------------- | ----------------------------------- |
| `course_id`   | INTEGER  | PK, Auto-increment                           | Unique identifier for the course    |
| `subject_id`  | INTEGER  | FK → Subject(`subject_id`), NOT NULL         | The subject being taught            |
| `teacher_id`  | INTEGER  | FK → Teacher_Profile(`teacher_id`), NOT NULL | The teacher assigned to the course  |
| `batch_id`    | INTEGER  | FK → Batch(`batch_id`), NOT NULL             | The student batch taking the course |
| `staff_id`    | INTEGER  | FK → Staff_Profile(`staff_id`), NULLABLE     | The staff assigned to the course    |
| `description` | TEXT     |                                      | Brief course summary                |
| `semester`    | INTEGER  | NOT NULL         | Semester number (1 or 2)            |
| `year`        | INTEGER  | NOT NULL                                     | Academic year                       |
| `remarks`     | TEXT     |                                      | Extra notes                         |
| `created_at`  | DATETIME | DEFAULT CURRENT_TIMESTAMP                    | Timestamp                           |
| `modified_at` | DATETIME | ON UPDATE CURRENT_TIMESTAMP                  | Timestamp                           |

📌 **Constraint:** Unique on (`subject_id`, `teacher_id`, `batch_id`, `semester`, `year`)

---

### Table: `Enrollment`

Tracks student enrollment information in a course.

| Field             | Type        | Constraints                                        | Description                                                 |
| ----------------- | ----------- | -------------------------------------------------- | ----------------------------------------------------------- |
| `enrollment_id`   | INTEGER     | PK, Auto-increment                                 | Unique ID                                                   |
| `student_id`      | INTEGER     | FK → Student_Profile(student_id)                   | The student                                                 |
| `course_id`       | INTEGER     | FK → Course(course_id)                             | The course                                                  |
| `enrollment_date` | DATE        |                                            | Date enrolled                                               |
| `status`          | VARCHAR(20) |  | Status of the enrollment (e.g., Active, Completed, Dropped) |
| `grade`           | VARCHAR(2)       |                                            | Final grade (e.g. A, B, C, ... etc.)                                                 |
| `rank`            | INTEGER     |                                            | Class rank                                                  |
| `remark`          | TEXT        |                                            | Additional Notes                                            |
| `created_at`      | DATETIME    | DEFAULT CURRENT_TIMESTAMP                          | Timestamp                                                   |
| `modified_at`     | DATETIME    | ON UPDATE CURRENT_TIMESTAMP                        | Timestamp                                                   |

📌 **Constraint:** Unique on (`student_id`, `course_id`)

---

### Table: `Assessment`

Stores individual scores for a student's course performance.

| Field           | Type        | Constraints                    | Description                                                                                                      |
| --------------- | ----------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| `assessment_id` | INTEGER     | PK, Auto-increment             | Unique ID                                                                                                        |
| `enrollment_id` | INTEGER     | FK → Enrollment(enrollment_id) | Student-course relation                                                                                          |
| `type`          | VARCHAR(30) |                                | Type of assessment (e.g. quiz, mid, final, assignment)                                                           |
| `score`         | FLOAT       | NOT NULL                       | Score achieved                                                                                                   |
| `total_score`   | FLOAT       | NOT NULL                       | Total Score of the assessment (e.g. if the student score 30/50, here the `score` is 30, and `total_score` is 50) |
| `given_at`      | DATE        | NOT NULL                       | Date assessment was given                                                                                        |
| `remarks`       | TEXT        |                        | Additional Notes                                                                                                 |
| `created_at`    | DATETIME    | DEFAULT CURRENT_TIMESTAMP      | Timestamp                                                                                                        |
| `modified_at`   | DATETIME    | ON UPDATE CURRENT_TIMESTAMP    | Timestamp                                                                                                        |

---

## 🔗 Relationships Summary

### One-to-One

- `User` → `Teacher_Profile`
- `User` → `Student_Profile`
- `User` → `Staff_Profile`

### One-to-Many

- `User` → `Emergency_Contact`
- `User` → `Address`
- `Emergency_Contact` → `Address`
- `Department` → `Subject`
- `Subject` → `Course`
- `Batch` → `Course`
- `Batch` → `Student_Profile`
- `Teacher_Profile` → `Course`
- `Staff_Profile` → `Course`
- `Course` → `Enrollment`
- `Student_Profile` → `Enrollment`
- `Enrollment` → `Assessment`

### Many-to-Many (via associative table)

- `User` → `User_Role` ←  `Role`

---

## 🗒️ Additional Notes

- All dates are to be in Ethiopian Calendar

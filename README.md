# Ewket Birhane Sunday School - Student Management System (SMS)

## 📝 Description

Ewket Birhane is a Sunday School within the Ethiopian Orthodox Tewahedo Church, located at the Salite Mehret Saint Mary and Saint Kirstos Semra Church, Addis Ababa, Ethiopia. The school teaches theological courses as well as various life skill trainings to students. It also allows students to participate in community services and outreach programs, which helps to foster a sense of social responsibility and spiritual growth.

I have been a part of the school for a few years now, both as a student and a class coordinator and I can attest to the positive impact it has had on my life. While learning and serving there I have noticed a lack of centralized student management system in managing the students, teachers and courses. The school teaches about 2000+ students each year, so it is important to have a student management system in order to manage and effectively administer the students and teachers.

To address this challenge, this project aims to develop a robust Student Management System (SMS) tailored to the needs of Ewket Birhane. The system will help streamline administrative tasks, improve data organization, and enhance the overall learning experience for both students, teachers and administrators.

## ✨ Features

- **User Management**:
  - Custom user model with roles (Student, Teacher, Staff, etc.).
  - Role-based access control.
- **Profiles**:
  - Student, Teacher, and Staff profiles.
- **Academic Management**:
  - Batches, Courses, Enrollments, and Assessments.
- **Emergency Contacts**:
  - Emergency contact information for users.
- **Address Management**:
  - User and emergency contact addresses.

## 🚀 How to Run the Project

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd Ewket_Birhane_SMS
   ```

2. **Set Up a Virtual Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   Open your browser and go to `http://127.0.0.1:8000/`.

## 📄 Documentation

- **Core Models Documentation**: [docs/core_models_documentation.md](./docs/core_models_documentation.md)
- **Database Design Documentation**: [docs/database_design_documentation.md](./docs/database_design_documentation.md)
- **Entity Relationship Diagram (ERD)**: [docs/ERD_v7_Final.png](./docs/ERD_v7_Final.png)
- **API Documentation:** [docs/api_documentation.md](./docs/api_documentation.md)

## 🌱 Seeding Demo Data

To seed the database with demo data, use the [seed_demo_data.py](./data/seed_demo_data.py) script:

   ```bash
   python data/seed_demo_data.py
   ```

# 🎓 Learning Management System (LMS) API

A complete **Learning Management System (LMS)** Backend built with **Django** and **Django REST Framework**.

This project provides RESTful APIs for managing users, courses, lessons, enrollments, quizzes, and authentication using JWT.

---

# 🚀 Features

## Authentication

- User Registration
- User Login (JWT Authentication)
- Logout (JWT Blacklist)
- User Profile
- Change Password
- Forgot Password
- Reset Password
- Delete Account

---

## User Roles

There are two roles:

- Teacher
- Student

Permissions are handled according to each role.

---

## Courses

Teachers can:

- Create Course
- Update Course
- Delete Course

Students can:

- Browse Courses
- View Course Details

Features:

- Categories
- Slug
- Thumbnail
- Search
- Filtering
- Ordering
- Pagination

---

## Reviews

Students can:

- Add Review
- Rate Course

Features:

- One review per student per course
- Average rating

---

## Enrollments

Students can:

- Enroll in courses
- View enrolled courses

Features:

- Prevent duplicate enrollment
- List student enrollments

---

## Lessons

Teachers can:

- Create Lessons
- Update Lessons
- Delete Lessons

Students can:

- View lessons of enrolled courses

Features:

- Video URL
- PDF Attachment
- Lesson Ordering
- Preview Lessons

---

## Quizzes

Teachers can:



Students can:

- Get Score

---

# 🛠 Built With

- Python
- Django
- Django REST Framework
- Simple JWT

- PostgreSQL (Production Ready)
- Pillow
- Django Filter

---

# 📂 Project Structure

```
LMS/
│
├── users/
├── courses/
├── enrollments/
├── lessons/
│
├── config/
│
├── manage.py
└── requirements.txt
```

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/lms-api.git
```

Move into project

```bash
cd lms-api
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```




Apply migrations

```bash
python manage.py migrate
```

Create superuser

```bash
python manage.py createsuperuser
```

Run server

```bash
python manage.py runserver
```

---

# 🔑 Authentication

Authentication is implemented using JWT.

Login returns:

```json
{
    "refresh": "...",
    "access": "..."
}
```

Authenticated endpoints require:

```
Authorization: Bearer <access_token>
```

---

# 📖 API Endpoints

## Authentication

| Method | Endpoint |
|----------|-------------------------|
| POST | /api/register/ |
| POST | /api/login/ |
| POST | /api/logout/ |
| GET | /api/profile/ |
| PUT | /api/change-password/ |
| POST | /api/forgot-password/ |
| PUT | /api/reset-password/<uuid>/ |
| DELETE | /api/delete-account/ |

---

## Courses

| Method | Endpoint |
|----------|---------------------|
| GET | /api/courses/ |
| POST | /api/courses/ |
| GET | /api/courses/<slug>/ |
| PATCH | /api/courses/<slug>/ |
| DELETE | /api/courses/<slug>/ |

---

## Categories

| Method | Endpoint |
|----------|----------------------|
| GET | /api/categories/ |
| POST | /api/categories/ |

---

## Reviews

| Method | Endpoint |
|----------|----------------------|
| POST | /api/reviews/ |

---

## Enrollments

| Method | Endpoint |
|----------|--------------------------|
| POST | /api/enrollments/ |
| GET | /api/enrollments/ |

---

## Lessons

| Method | Endpoint |
|----------|--------------------------|
| GET | /api/lessons/ |
| POST | /api/lessons/ |
| GET | /api/lessons/<id>/ |
| PATCH | /api/lessons/<id>/ |
| DELETE | /api/lessons/<id>/ |

---

---

# 🔒 Permissions

### Teacher

- Create Courses
- Update Courses
- Delete Courses
- Create Lessons
- Manage Lessons


### Student

- Browse Courses
- Enroll Courses
- Watch Lessons

- Add Reviews

---

# ✅ Validation

Examples:

- Password must contain:
    - Uppercase letter
    - Lowercase letter
    - Number
    - Minimum 8 characters

- Duplicate enrollment is prevented.

- Duplicate review is prevented.

- Course price cannot be negative.

---

# 🧪 Testing

The project includes API tests for:

- Authentication
- Password Reset
- Courses
- Enrollments
- Lessons


```bash
python manage.py test
```

---

# 📚 API Documentation

Swagger UI

```
/api/schema/swagger-ui/


```
/api/schema/redoc/
```

---

---

# 🔮 Future Improvements

- Payment Integration (Stripe / Paymob)
- Shopping Cart
- Wishlist
- Certificates
- Email Verification
- Notifications
- Redis Caching
- Celery Background Tasks

---

# 👨‍💻 Author

**Mostafa Salim**

Backend Developer

Python | Django | Django REST Framework

GitHub:
[https://github.com/yourusername](https://github.com/Mustafa00Salem/Learning-Management-System-LMS-/)

LinkedIn:
[https://linkedin.com/in/yourusername](https://www.linkedin.com/in/mustafa-ali-30564533b/)

---

# ⭐ If you like this project, don't forget to give it a star.

# Shebaa247 Job Portal API

A Django Rest Framework based API for a Job Portal.

## Features

### Authentication
- Custom user model with email authentication
- JWT token based authorization
- Password reset with secure tokens
- OTP verification system
- Three user types: Job Seeker, Employer, Admin

### API Endpoints

#### Auth Endpoints
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout
- `POST /api/auth/logout/all/` - Logout from all devices
- `POST /api/auth/token/refresh/` - Refresh JWT token
- `POST /api/auth/password/reset/` - Request password reset
- `POST /api/auth/password/reset/confirm/` - Confirm password reset
- `POST /api/auth/password/change/` - Change password
- `POST /api/auth/password/change/confirm/` - Confirm password change
- `POST /api/auth/account/delete/` - Delete user account
- `POST /api/auth/account/delete/confirm/` - Confirm account deletion

#### OTP Endpoints
- `POST /api/auth/otp/request/` - Request OTP
- `POST /api/auth/otp/verify/` - Verify OTP

## Project Authentication Status
- ✅ User Authentication
- ✅ Password Reset
- ✅ OTP System
- ⏳ Email Verification
- ⏳ User Profiles

## Tech Stack
- Django 4.2
- Django Rest Framework
- SimpleJWT
- SQLite (Development)

## Directory Structure

```
Shebaa247-API/
├── Shebaa247/
│   ├── __init__.py
│   ├── asgi.py
│   ├── auth_settings.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── auth_api/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   ├── urls.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user_model.py
│   │   └── otp_model.py
│   │
│   ├── serializers/
│   │   ├── __init__.py
│   │   ├── account_deletion_serializer.py
│   │   ├── login_serializer.py
│   │   ├── logout_serializer.py
│   │   ├── register_serializer.py
│   │   ├── otp_serializer.py
│   │   ├── password_reset_serializer.py
│   │   └── password_change_serializer.py
│   │
│   └── views/
│       ├── __init__.py
│       ├── account_deletion_view.py
│       ├── login_view.py
│       ├── logout_view.py
│       ├── register_view.py
│       ├── otp_view.py
│       ├── password_reset_view.py
│       └── password_change_view.py
│
├── profiles/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   ├── urls.py
│   ├── utils.py
│   ├── views.py
│   │
│   └── models/
│       ├── __init__.py
│       ├── base_profile.py
│       │
│       ├── employer/
│       │   ├── __init__.py
│       │   └── employer_profile.py
│       │
│       └── jobseeker/
│           ├── __init__.py
│           ├── profile.py
│           ├── status_choice.py
│           ├── user_education.py
│           └── work_experience.py
│
├── .gitignore
├── README.md
├── manage.py
├── pyrightconfig.json
├── requirements.txt
└── requirements-dev.txt

The project is still under development. More features will be added soon. Stay tuned!

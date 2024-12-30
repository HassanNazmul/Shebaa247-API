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
- `POST /api/auth/token/refresh/` - Refresh JWT token
- `POST /api/auth/password/reset/` - Request password reset
- `POST /api/auth/password/reset/confirm/` - Confirm password reset

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
│   ├── auth_settings.py      # Custom authentication settings
│   ├── settings.py           # Main settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py
│
├── auth_api/
│   ├── __init__.py
│   ├── admin.py             # Admin configurations
│   ├── apps.py
│   │
│   ├── models/              # Models directory
│   │   ├── __init__.py
│   │   ├── user_model.py    # Custom user model
│   │   └── otp_model.py     # OTP model
│   │
│   ├── serializers/         # Serializers directory
│   │   ├── __init__.py
│   │   ├── login_serializer.py
│   │   ├── register_serializer.py
│   │   ├── otp_serializer.py
│   │   └── password_reset_serializer.py
│   │
│   ├── views/               # Views directory
│   │   ├── __init__.py
│   │   ├── login_view.py
│   │   ├── register_view.py
│   │   ├── otp_view.py
│   │   └── password_reset_view.py
│   │
│   ├── tests.py
│   └── urls.py              # Auth API URLs
│
├── .gitignore
├── README.md
├── manage.py
├── pyrightconfig.json
└── requirements.txt

The project is still under development. More features will be added soon. Stay tuned!

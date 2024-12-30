```markdown
# Shebaa247 Job Portal API

A Django Rest Framework based API for a Job Portal.

## Features

### Custom User Authentication
- Email-based authentication (no username)
- Three user types: Job Seeker, Employer, and Admin
- JWT (JSON Web Token) based authentication
- Custom user model with email as the unique identifier

### Authentication Endpoints
1. **Registration**
   - Endpoint: `POST /api/auth/register/`
   - Fields: email, password, password2, user_type
   - Creates new user account

2. **Login**
   - Endpoint: `POST /api/auth/login/`
   - Fields: email, password
   - Returns JWT access and refresh tokens

3. **Token Refresh**
   - Endpoint: `POST /api/auth/token/refresh/`
   - Fields: refresh token
   - Returns new access token

### OTP Verification System
- 7-digit OTP generation
- 5-minute expiration time
- Verification status tracking
- Email-based OTP delivery (to be implemented)

#### OTP Endpoints
1. **Request OTP**
   - Endpoint: `POST /api/auth/otp/request/`
   - Fields: email
   - Generates OTP for registered users

2. **Verify OTP**
   - Endpoint: `POST /api/auth/otp/verify/`
   - Fields: email, code
   - Verifies submitted OTP

## Technical Stack

- Python 3.x
- Django 4.2
- Django Rest Framework
- SimpleJWT for JWT authentication
- SQLite (development)

## Security Features

- JWT authentication with refresh tokens
- Password validation
- OTP expiration
- Admin panel security measures
- CORS configuration
- Rate limiting

## Development Status

- ✅ Custom User Model
- ✅ JWT Authentication
- ✅ OTP System
- ⏳ Email Verification
- ⏳ Password Reset
- ⏳ User Profiles

## Project Structure

Shebaa247-API/
├── auth_api/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user_model.py
│   │   └── otp_model.py
│   ├── serializers/
│   │   ├── __init__.py
│   │   ├── login_serializer.py
│   │   ├── register_serializer.py
│   │   └── otp_serializer.py
│   ├── views/
│   │   ├── __init__.py
│   │   ├── login_view.py
│   │   ├── register_view.py
│   │   └── otp_view.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   └── urls.py
├── Shebaa247/
│   ├── __init__.py
│   ├── asgi.py
│   ├── auth_settings.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .gitignore
├── manage.py
├── pyrightconfig.json
├── README.md
└── requirements.txt

The project is still under development. More features will be added soon. Stay tuned!

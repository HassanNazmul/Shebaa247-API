from datetime import timedelta

# Debug Setting
DEBUG = True

# OAuth2 Settings
OAUTH2_SETTINGS = {
    # Token Settings
    'ACCESS_TOKEN_EXPIRE_SECONDS': 900,  # 15 minutes (shorter time for better security)
    'REFRESH_TOKEN_EXPIRE_SECONDS': 43200,  # 12 hours
    'ROTATE_REFRESH_TOKEN': True,  # Generate new refresh token when used
    'REUSE_REFRESH_TOKEN': False,  # Don't reuse refresh tokens

    # Scope Settings
    'SCOPES': {
        # Job Seeker Scopes
        'profile:read': 'Read own profile', # Read own profile
        'profile:write': 'Update own profile',  # Update own profile
        'jobs:view': 'View job listings',  # View job listings
        'jobs:apply': 'Apply for jobs', # Apply for jobs
        'applications:read': 'View own job applications',   # View own job applications

        # Employer Scopes
        'company:read': 'Read company profile', # Read company profile
        'company:write': 'Update company profile',  # Update company profile
        'jobs:post': 'Post new jobs',   # Post new jobs
        'jobs:manage': 'Manage job posts',  # Manage job posts
        'applications:manage': 'Manage received applications',  # Manage received applications
    },

    # Default Scopes
    'DEFAULT_SCOPES': ['profile:read', 'jobs:view'],  # Minimal default access

    # Security Settings
    'REQUIRE_HTTPS': True,  # Force HTTPS only
    'AUTHORIZATION_CODE_EXPIRE_SECONDS': 300,  # 5 minutes
    'REFRESH_TOKEN_GRACE_PERIOD_SECONDS': 120,  # 2 minutes grace period

    # Token Settings
    'ACCESS_TOKEN_METHOD': 'POST',  # Restrict to POST method
    'PKCE_REQUIRED': True,  # Require PKCE (Proof Key for Code Exchange)

    # Rate Limiting
    'RATELIMIT_ENABLE': True,
    'RATELIMIT_RATE': '5/min',  # 5 attempts per minute
    'RATELIMIT_BLOCK_TIME': 300,  # 5 minutes block after limit exceeded

    # Additional Security
    'ERROR_RESPONSE_WITH_SCOPES': True,  # Include required scopes in error responses
    'STRICT_HTTPS': True,  # Stricter HTTPS checking
    'ALLOWED_REDIRECT_URI_SCHEMES': ['https'],  # Only allow HTTPS redirects

    # Token Management
    'REFRESH_TOKEN_EXPIRE_ON_CLIENT_DELETE': True,
    'REFRESH_TOKEN_EXPIRE_ON_PASSWORD_CHANGE': True,
}

# Additional Security Settings
REST_FRAMEWORK_SETTINGS = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '100/day',
        'user': '1000/day'
    }
}

# Security Headers Settings
SECURITY_SETTINGS = {
    'SECURE_BROWSER_XSS_FILTER': True,
    'SECURE_CONTENT_TYPE_NOSNIFF': True,
    'SECURE_HSTS_SECONDS': 31536000,
    'SECURE_HSTS_INCLUDE_SUBDOMAINS': True,
    'SECURE_HSTS_PRELOAD': True,
    'SECURE_SSL_REDIRECT': False if DEBUG else True,  # Disable in development
    'SESSION_COOKIE_SECURE': False if DEBUG else True,  # Disable in development
    'CSRF_COOKIE_SECURE': False if DEBUG else True,  # Disable in development
}

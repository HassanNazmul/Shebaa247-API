from datetime import timedelta

# Debug Setting
DEBUG = True

# JWT Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60), # 1 hour
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),    # 1 day
    'ROTATE_REFRESH_TOKENS': False, # If True, old refresh tokens will be deleted on refresh
    'BLACKLIST_AFTER_ROTATION': True,   # If True, old refresh tokens will be blacklisted after rotation
    'UPDATE_LAST_LOGIN': False, # If True, the last_login field of the user will be updated on every request to the server

    'ALGORITHM': 'HS256',   # Algorithm used to sign the token
    'VERIFYING_KEY': None,  # If None, the value of SIGNING_KEY will be used
    'AUDIENCE': None,   # The audience claim (aud)
    'ISSUER': None, # The issuer claim (iss)

    'SIGNING_KEY': 'Lnu6J9S79Tfd5A1mCGCwAJTCnz7LIH7eFr2M4-H5xvaMiszzUMfXcRX38V4u61vwEiTqxLBi4gGOqnk0SmFAZw',  # Replace with your actual secret key

    'AUTH_HEADER_TYPES': ('Bearer',),   # The type of the auth header
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',   # The name of the auth header
    'USER_ID_FIELD': 'id',  # The field used as the user identifier
    'USER_ID_CLAIM': 'user_id', # The claim used as the user identifier
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule', # The method used to authenticate the user

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',), # The token classes that this backend can mint
    'TOKEN_TYPE_CLAIM': 'token_type',   # The claim that will be used to determine the token type

    'JTI_CLAIM': 'jti', # The claim used for the token ID
}

# Rest Framework Settings
REST_FRAMEWORK_SETTINGS = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
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

# CORS Settings
CORS_SETTINGS = {
    'CORS_ALLOW_ALL_ORIGINS': False,  # Set to True only for development
    'CORS_ALLOWED_ORIGINS': [
        'http://localhost:3000',
    ],
    'CORS_ALLOW_CREDENTIALS': True,
    'CORS_ALLOW_METHODS': [
        'GET',
        'POST',
        'PUT',
        'PATCH',
        'DELETE',
        'OPTIONS',
    ],
    'CORS_ALLOW_HEADERS': [
        'authorization',  # For JWT tokens
        'content-type',  # For specifying JSON content
        'x-csrftoken',   # For CSRF protection
    ],
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

from datetime import timedelta

# Debug Setting
DEBUG = True

# JWT Settings
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),  # ⬅️ Reduce from 60 to 15 minutes
    'REFRESH_TOKEN_LIFETIME': timedelta(days=14),    # ⬅️ Increase from 1 to 14 days
    'ROTATE_REFRESH_TOKENS': True,                   # ⬅️ Enable token rotation
    'BLACKLIST_AFTER_ROTATION': True,                # ⬅️ Blacklist old tokens after rotation

    'UPDATE_LAST_LOGIN': True,                      # ⬅️ Track login times

    'AUTH_COOKIE': 'refresh_token',                 # ⬅️ Cookie name for refresh token
    'AUTH_COOKIE_SECURE': True,                     # ⬅️ Only send cookie over HTTPS
    'AUTH_COOKIE_HTTP_ONLY': True,                  # ⬅️ Prevent JavaScript access
    'AUTH_COOKIE_PATH': '/',                        # ⬅️ Cookie path
    'AUTH_COOKIE_SAMESITE': 'Lax',                  # ⬅️ CSRF protection

    # Token Properties
    'TOKEN_OBTAIN_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenObtainPairSerializer',    # The serializer used to obtain a token
    'TOKEN_REFRESH_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenRefreshSerializer',      # The serializer used to refresh a token
    'TOKEN_VERIFY_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenVerifySerializer',        # The serializer used to verify a token
    'TOKEN_BLACKLIST_SERIALIZER': 'rest_framework_simplejwt.serializers.TokenBlacklistSerializer',  # The serializer used to blacklist a token

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
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '20/minute',  # ⬅️ More strict rate limiting
        'user': '60/minute'   # ⬅️ More strict rate limiting
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

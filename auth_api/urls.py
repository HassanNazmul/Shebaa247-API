# auth_api/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    LoginView,
    RegisterView,
    RequestOTPView,
    VerifyOTPView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
    LogoutView,
    LogoutAllView,
    PasswordChangeRequestView,
    PasswordChangeConfirmView,
    AccountDeletionRequestView,
    AccountDeletionConfirmView,
)

app_name = 'auth_api'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/all/', LogoutAllView.as_view(), name='logout-all'),

    path('register/', RegisterView.as_view(), name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('otp/request/', RequestOTPView.as_view(), name='request-otp'),
    path('otp/verify/', VerifyOTPView.as_view(), name='verify-otp'),

    path('password/reset/',  PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),

    path('password/change/', PasswordChangeRequestView.as_view(), name='password-change-request'),
    path('password/change/confirm/', PasswordChangeConfirmView.as_view(), name='password-change-confirm'),

    path('account/delete/request/', AccountDeletionRequestView.as_view(), name='account-deletion-request'),
    path('account/delete/confirm/', AccountDeletionConfirmView.as_view(), name='account-deletion-confirm'),
]

# Future work
# Priority Implementation Order:
# 1. Email Verification (Most important)
# 2. Profile Management
# 3. Session Management
# 4. Security Features
# 5. Two-Factor Authentication
# 6. Account Recovery
# 7. Notification Preferences
# 8. API Access Management
# 9. Social Authentication
# 10. Audit and Compliance

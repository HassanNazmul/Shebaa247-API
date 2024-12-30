# auth_api/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import LoginView, RegisterView, RequestOTPView, VerifyOTPView

app_name = 'auth_api'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('otp/request/', RequestOTPView.as_view(), name='request-otp'),
    path('otp/verify/', VerifyOTPView.as_view(), name='verify-otp'),
]

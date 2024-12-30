# auth_api/views/otp_view.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model

from ..models import OTP
from ..serializers import OTPRequestSerializer, OTPVerifySerializer

User = get_user_model()

class RequestOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = OTPRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']

            # Check if user exists with this email
            if not User.objects.filter(email=email).exists():
                return Response({
                    "message": "No user found with this email address"
                }, status=status.HTTP_404_NOT_FOUND)

            # Delete any existing OTP
            OTP.objects.filter(email=email).delete()

            # Create new OTP
            otp = OTP.objects.create(
                email=email,
                code=OTP.generate_otp(),
                expires_at=timezone.now() + timedelta(minutes=5)
            )

            # In production, send OTP via email here
            return Response({
                "message": "OTP sent successfully",
                "email": email,
                "code": otp.code,  # Remove in production
                "expires_in": "5 minutes"
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "Invalid email format"
        }, status=status.HTTP_400_BAD_REQUEST)

class VerifyOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = OTPVerifySerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            code = serializer.validated_data['code']

            try:
                otp = OTP.objects.get(email=email, code=code, is_verified=False)

                if otp.is_expired():
                    return Response({
                        "message": "OTP has expired"
                    }, status=status.HTTP_400_BAD_REQUEST)

                otp.is_verified = True
                otp.save()

                return Response({
                    "message": "OTP verified successfully"
                }, status=status.HTTP_200_OK)

            except OTP.DoesNotExist:
                return Response({
                    "message": "Invalid OTP"
                }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "message": "Invalid input format"
        }, status=status.HTTP_400_BAD_REQUEST)

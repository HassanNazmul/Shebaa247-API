# auth_api/views/otp_view.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.utils import timezone
from datetime import timedelta
from ..models.otp import OTP
from ..serializers.otp_serializer import OTPRequestSerializer, OTPVerifySerializer

class RequestOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = OTPRequestSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']

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
                "code": otp.code  # Remove in production
            })
        return Response(serializer.errors, status=400)

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
                    }, status=400)

                otp.is_verified = True
                otp.save()

                return Response({
                    "message": "OTP verified successfully"
                })

            except OTP.DoesNotExist:
                return Response({
                    "message": "Invalid OTP"
                }, status=400)

        return Response(serializer.errors, status=400)

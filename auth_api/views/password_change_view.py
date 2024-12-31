# auth_api/views/password_change_view.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import timedelta
from ..models import OTP
from ..serializers.password_change_serializer import PasswordChangeRequestSerializer, PasswordChangeConfirmSerializer

class PasswordChangeRequestView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PasswordChangeRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user

            # Delete any existing OTP
            OTP.objects.filter(email=user.email).delete()

            # Create new OTP
            otp = OTP.objects.create(
                email=user.email,
                code=OTP.generate_otp(),
                expires_at=timezone.now() + timedelta(minutes=5)
            )

            # In production, send OTP via email here
            return Response({
                "message": "OTP sent to your email",
                "email": user.email,
                "code": otp.code,  # Remove in production
                "expires_in": "5 minutes"
            }, status=status.HTTP_200_OK)

        return Response({
            "message": "Invalid current password"
        }, status=status.HTTP_400_BAD_REQUEST)

class PasswordChangeConfirmView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PasswordChangeConfirmSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = request.user
            otp_code = serializer.validated_data['otp']
            new_password = serializer.validated_data['new_password']

            try:
                otp = OTP.objects.get(
                    email=user.email,
                    code=otp_code,
                    is_verified=False
                )

                if otp.is_expired():
                    return Response({
                        "message": "OTP has expired"
                    }, status=status.HTTP_400_BAD_REQUEST)

                # Change password
                user.set_password(new_password)
                user.save()

                # Mark OTP as verified
                otp.is_verified = True
                otp.save()

                # In production, send confirmation email here

                # Optional: Logout from all devices
                from rest_framework_simplejwt.tokens import OutstandingToken, BlacklistedToken
                tokens = OutstandingToken.objects.filter(user=user)
                for token in tokens:
                    BlacklistedToken.objects.get_or_create(token=token)

                return Response({
                    "message": "Password changed successfully. Please login again."
                }, status=status.HTTP_200_OK)

            except OTP.DoesNotExist:
                return Response({
                    "message": "Invalid OTP"
                }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "message": "Invalid input",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

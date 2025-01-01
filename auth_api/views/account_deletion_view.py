# auth_api/views/account_deletion_view.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from datetime import timedelta
from ..models import OTP
from ..serializers import AccountDeletionRequestSerializer, AccountDeletionConfirmSerializer

class AccountDeletionRequestView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AccountDeletionRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                user = request.user

                # Verify password
                if not user.check_password(serializer.validated_data['password']):
                    return Response({
                        "message": "Invalid password"
                    }, status=status.HTTP_400_BAD_REQUEST)

                # Generate OTP
                OTP.objects.filter(email=user.email).delete()
                otp = OTP.objects.create(
                    email=user.email,
                    code=OTP.generate_otp(),
                    expires_at=timezone.now() + timedelta(minutes=5)
                )

                # In production, send warning email with OTP
                return Response({
                    "message": "Please verify your account deletion request",
                    "email": user.email,
                    "code": otp.code,  # Remove in production
                    "expires_in": "5 minutes"
                }, status=status.HTTP_200_OK)

            return Response({
                "message": "Invalid password format",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "message": "An error occurred while processing your request"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class AccountDeletionConfirmView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AccountDeletionConfirmSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        try:
            if serializer.is_valid():
                user = request.user

                try:
                    # Verify OTP
                    otp = OTP.objects.get(
                        email=user.email,
                        code=serializer.validated_data['otp'],
                        is_verified=False
                    )

                    if otp.is_expired():
                        return Response({
                            "message": "OTP has expired. Please request a new one"
                        }, status=status.HTTP_400_BAD_REQUEST)

                    # Delete account
                    user.delete_account()

                    # Mark OTP as verified
                    otp.is_verified = True
                    otp.save()

                    return Response({
                        "message": "Account deleted successfully"
                    }, status=status.HTTP_200_OK)

                except OTP.DoesNotExist:
                    return Response({
                        "message": "Invalid OTP or OTP not found"
                    }, status=status.HTTP_400_BAD_REQUEST)

            return Response({
                "message": "Invalid input format",
                "errors": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "message": "An error occurred while processing your request"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

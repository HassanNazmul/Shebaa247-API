# auth_api/views/password_reset_view.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from ..serializers.password_reset_serializer import (
    PasswordResetRequestSerializer,
    PasswordResetConfirmSerializer
)

User = get_user_model()

class PasswordResetRequestView(APIView):
    permission_classes = [AllowAny]
    serializer_class = PasswordResetRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']

            try:
                user = User.objects.get(email=email)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                token = default_token_generator.make_token(user)

                reset_link = f"/reset-password/{uid}/{token}/"

                return Response({
                    "message": "Password reset link sent",
                    "uid": uid,
                    "token": token,
                    "reset_link": reset_link
                }, status=status.HTTP_200_OK)

            except User.DoesNotExist:
                return Response({
                    "message": "No user found with this email"
                }, status=status.HTTP_404_NOT_FOUND)

        return Response({
            "message": "Invalid email format"
        }, status=status.HTTP_400_BAD_REQUEST)

class PasswordResetConfirmView(APIView):
    permission_classes = [AllowAny]
    serializer_class = PasswordResetConfirmSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                uid = force_str(urlsafe_base64_decode(serializer.validated_data['uid']))
                user = User.objects.get(pk=uid)
                token = serializer.validated_data['token']

                if not default_token_generator.check_token(user, token):
                    return Response({
                        "message": "Invalid or expired reset link"
                    }, status=status.HTTP_400_BAD_REQUEST)

                user.set_password(serializer.validated_data['new_password'])
                user.save()

                return Response({
                    "message": "Password reset successful"
                }, status=status.HTTP_200_OK)

            except (TypeError, ValueError, OverflowError, User.DoesNotExist):
                return Response({
                    "message": "Invalid reset link"
                }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "message": "Invalid input",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

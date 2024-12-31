# auth_api/views/logout_view.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from ..serializers.logout_serializer import LogoutSerializer


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutSerializer

    def post(self, request):
        try:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                # Blacklist the refresh token
                token = RefreshToken(serializer.validated_data['refresh'])
                token.blacklist()

                return Response({
                    "message": "You have successfully logged out."
                }, status=status.HTTP_200_OK)

            return Response({
                "error": "Invalid token."
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({
                "error": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class LogoutAllView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Get all refresh tokens for user and blacklist them
            tokens = RefreshToken.for_user(request.user)
            for token in tokens:
                token.blacklist()

            return Response({
                "message": "Logged out from all devices successfully"
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                "message": "Something went wrong"
            }, status=status.HTTP_400_BAD_REQUEST)

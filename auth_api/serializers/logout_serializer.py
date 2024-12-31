# auth_api/serializers/logout_serializer.py
from rest_framework import serializers

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField() # refresh token

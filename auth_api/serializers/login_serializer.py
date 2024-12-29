# auth_api/serializers/login_serializer.py
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            data = super().validate(attrs)
            data.update({
                'email': self.user.email,
                'user_type': self.user.user_type,
                'is_active': self.user.is_active,
            })
            return data
        except Exception as e:
            raise serializers.ValidationError({
                "error": "Invalid credentials or inactive account"
            })

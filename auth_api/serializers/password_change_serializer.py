# auth_api/serializers/password_change_serializer.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class PasswordChangeRequestSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)

    def validate_current_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError("Current password is incorrect")
        return value

class PasswordChangeConfirmSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=7)
    new_password = serializers.CharField(validators=[validate_password])
    confirm_password = serializers.CharField()

    def validate(self, attrs):
        if attrs['new_password'] != attrs['confirm_password']:
            raise serializers.ValidationError({
                "message": "Password fields didn't match."
            })
        return attrs

# auth_api/serializers/account_deletion_serializer.py
from rest_framework import serializers

class AccountDeletionRequestSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)

class AccountDeletionConfirmSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=7)

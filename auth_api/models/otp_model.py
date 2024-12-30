# auth_api/models/otp.py
from django.db import models
from django.utils import timezone
import random

class OTP(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=7)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()

    class Meta:
        indexes = [
            models.Index(fields=['email', 'code', 'is_verified']),
        ]

    def __str__(self):
        return f"{self.email} - {self.code}"

    @staticmethod
    def generate_otp():
        """Generate a 7 digit OTP"""
        return str(random.randint(1000000, 9999999))

    def is_expired(self):
        """Check if OTP is expired"""
        return timezone.now() > self.expires_at

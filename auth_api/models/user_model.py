# auth_api/models.py
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Force admin type and other required fields for superuser
        extra_fields.setdefault('user_type', 'ADMIN')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('user_type') != 'ADMIN':
            raise ValueError('Superuser must have user_type=ADMIN.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('JOBSEEKER', 'Job Seeker'),
        ('EMPLOYER', 'Employer'),
        ('ADMIN', 'Admin'),
    )

    email = models.EmailField(
        unique=True,
        verbose_name='email address',
        error_messages={
            'unique': 'A user with that email already exists.',
        }
    )
    user_type = models.CharField(
        max_length=9,
        choices=USER_TYPE_CHOICES
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def save(self, *args, **kwargs):
        if self.is_superuser and self.user_type != 'ADMIN':
            self.user_type = 'ADMIN'
        super().save(*args, **kwargs)

    def delete_account(self):
        super().delete()

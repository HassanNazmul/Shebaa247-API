# auth_api/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User, OTP

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'user_type', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('user_type', 'is_active', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('email',)

    # Fields shown when editing a user
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        (_('User Type'), {
            'fields': ('user_type',)
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions',
            ),
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
    )

    # Fields shown when creating a new user
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_type', 'password1', 'password2',),
        }),
    )

    filter_horizontal = ('groups', 'user_permissions',)


@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ('email', 'code', 'is_verified', 'is_valid_otp', 'created_at', 'expires_at')
    list_filter = ('is_verified', 'created_at', 'expires_at')
    search_fields = ('email', 'code')
    readonly_fields = ('created_at', 'expires_at', 'is_valid_otp')
    ordering = ('-created_at',)

    def is_valid_otp(self, obj):
        """
        Custom method to show if OTP is currently valid
        Returns: Boolean indicating if OTP is valid (not expired and not verified)
        """
        if obj.is_verified:
            return False
        return not obj.is_expired()

    is_valid_otp.boolean = True  # Shows as icon instead of True/False text
    is_valid_otp.short_description = 'Is Valid'  # Column header in admin

    def has_add_permission(self, request):
        # Prevent manual OTP creation from admin
        return False

    def has_change_permission(self, request, obj=None):
        # Prevent editing OTPs
        return False

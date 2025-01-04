# profiles/admin.py
from django.contrib import admin
from .models import (
    JobSeekerProfile,
    Education,
    WorkExperience
)

class EducationInline(admin.StackedInline):
    model = Education
    extra = 0  # No extra empty forms
    can_delete = True
    show_change_link = True
    classes = ['collapse']
    verbose_name = "Education"
    verbose_name_plural = "Education History"

class WorkExperienceInline(admin.StackedInline):
    model = WorkExperience
    extra = 0  # No extra empty forms
    can_delete = True
    show_change_link = True
    classes = ['collapse']
    verbose_name = "Work Experience"
    verbose_name_plural = "Work Experience History"

@admin.register(JobSeekerProfile)
class JobSeekerProfileAdmin(admin.ModelAdmin):
    # Display fields in list view
    list_display = [
        'user',
        'headline',
        'experience_level',
        'employment_status',
        'is_featured',
        'profile_visibility',
        'profile_completion',
        'last_active'
    ]

    # Filters in right sidebar
    list_filter = [
        'experience_level',
        'employment_status',
        'is_featured',
        'profile_visibility',
        'job_alert_active',
        'willing_to_relocate',
        'profile_searchable'
    ]

    # Search fields
    search_fields = [
        'user__email',
        'first_name',
        'last_name',
        'headline',
        'current_position',
        'current_company'
    ]

    # Organize fields in detail view
    fieldsets = (
        ('User Information', {
            'fields': (
                'user',
                'first_name',
                'last_name',
                'phone_number',
                'profile_picture'
            )
        }),
        ('Professional Information', {
            'fields': (
                'headline',
                'summary',
                'experience_level',
                'current_position',
                'current_company'
            )
        }),
        ('Skills & Expertise', {
            'classes': ('collapse',),
            'fields': (
                'skills',
                'languages',
                'certifications'
            )
        }),
        ('Job Preferences', {
            'classes': ('collapse',),
            'fields': (
                'job_types',
                'preferred_locations',
                'willing_to_relocate',
                'preferred_industries',
                'preferred_work_environment'
            )
        }),
        ('Salary Details', {
            'classes': ('collapse',),
            'fields': (
                'expected_salary_minimum',
                'expected_salary_maximum',
                'salary_currency',
                'salary_visibility'
            )
        }),
        ('Availability', {
            'fields': (
                'employment_status',
                'notice_period',
                'available_from'
            )
        }),
        ('Documents', {
            'classes': ('collapse',),
            'fields': (
                'cv',
                'cover_letter',
                'portfolio_link',
                'additional_documents'
            )
        }),
        ('Professional Links', {
            'classes': ('collapse',),
            'fields': (
                'linkedin_profile',
                'github_profile',
                'personal_website'
            )
        }),
        ('Privacy & Settings', {
            'fields': (
                'profile_visibility',
                'job_alert_active',
                'profile_searchable',
                'is_featured'
            )
        }),
        ('System Information', {
            'classes': ('collapse',),
            'fields': (
                'profile_completion',
                'last_job_application',
                'total_job_applications',
                'last_active',
                'date_joined',
                'updated_at'
            )
        }),
        ('Achievements', {
            'classes': ('collapse',),
            'fields': ('achievements',)
        })
    )

    # Read-only fields
    readonly_fields = [
        'profile_completion',
        'last_active',
        'date_joined',
        'updated_at',
        'total_job_applications'
    ]

    # Inline related models
    inlines = [EducationInline, WorkExperienceInline]

    # Save model customization
    def save_model(self, request, obj, form, change):
        if not change:  # If creating new object
            obj.calculate_profile_completion()
        super().save_model(request, obj, form, change)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = [
        'profile',
        'institution',
        'degree',
        'field_of_study',
        'start_date',
        'end_date',
        'current'
    ]
    list_filter = ['current', 'start_date', 'end_date']
    search_fields = ['institution', 'degree', 'field_of_study']
    ordering = ['-start_date']

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = [
        'profile',
        'company',
        'position',
        'start_date',
        'end_date',
        'current'
    ]
    list_filter = ['current', 'start_date', 'end_date']
    search_fields = ['company', 'position', 'responsibilities']
    ordering = ['-start_date']

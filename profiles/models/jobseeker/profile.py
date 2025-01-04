# profiles/models/profile.py
from django.db import models
from ..base_profile import BaseProfile
from .status_choice import (
    EXPERIENCE_CHOICES,
    EMPLOYMENT_STATUS,
    JOB_TYPE_CHOICES,
    WORK_ENVIRONMENT_CHOICES
)

class JobSeekerProfile(BaseProfile):
    # Professional Information
    headline = models.CharField(max_length=100, help_text="Professional headline")
    summary = models.TextField(blank=True, help_text="Professional summary")
    experience_level = models.CharField(
        max_length=20,
        choices=EXPERIENCE_CHOICES,
        default='entry'
    )
    current_position = models.CharField(max_length=100, blank=True)
    current_company = models.CharField(max_length=100, blank=True)

    # Skills and Expertise
    skills = models.JSONField(default=list, blank=True)
    languages = models.JSONField(default=list, blank=True)
    certifications = models.JSONField(default=list, blank=True)

    # Job Preferences
    job_types = models.JSONField(
        default=list,
        help_text="List of preferred job types"
    )
    preferred_locations = models.JSONField(
        default=list,
        help_text="List of preferred work locations"
    )
    willing_to_relocate = models.BooleanField(default=False)
    preferred_industries = models.JSONField(default=list, blank=True)
    preferred_work_environment = models.CharField(
        max_length=20,
        choices=WORK_ENVIRONMENT_CHOICES,
        default='office'
    )

    # Salary Expectations
    expected_salary_minimum = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    expected_salary_maximum = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    salary_currency = models.CharField(max_length=3, default='USD')

    # Availability
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_STATUS, default='actively_looking')
    notice_period = models.IntegerField(default=0, help_text="Notice period in days")
    available_from = models.DateField(null=True, blank=True)

    # Documents
    cv = models.FileField(upload_to='jobseeker/cvs/', null=True, blank=True)
    cover_letter = models.FileField(upload_to='jobseeker/cover_letters/', null=True, blank=True)
    portfolio_link = models.URLField(blank=True)

    # Social & Professional Links
    linkedin_profile = models.URLField(blank=True)
    github_profile = models.URLField(blank=True)
    personal_website = models.URLField(blank=True)

    # Privacy Settings
    profile_visibility = models.BooleanField(default=True, help_text="Profile visible to employers")
    salary_visibility = models.BooleanField(default=False, help_text="Salary expectations visible to employers")

    # System Fields
    is_featured = models.BooleanField(default=False)
    profile_completion = models.IntegerField(default=0)
    last_active = models.DateTimeField(auto_now=True)

    # Achievements
    achievements = models.JSONField(
        default=list,
        blank=True,
        help_text="List of professional achievements"
    )

    # Additional Documents
    additional_documents = models.JSONField(
        default=list,
        blank=True,
        help_text="List of additional document URLs"
    )

    # Preferences
    job_alert_active = models.BooleanField(
        default=True,
        help_text="Receive job alerts"
    )
    profile_searchable = models.BooleanField(
        default=True,
        help_text="Profile appears in search results"
    )

    # Meta Information
    last_job_application = models.DateTimeField(null=True, blank=True)
    total_job_applications = models.IntegerField(default=0)

    class Meta:
        ordering = ['-last_active']

    def __str__(self):
        return f"{self.user.email} - {self.headline}"

    def calculate_profile_completion(self):
        """Calculate profile completion percentage"""
        from profiles.utils import calculate_completion_percentage
        return calculate_completion_percentage(self)

    def get_active_applications(self):
        """Get list of active job applications"""
        return self.job_applications.filter(status='active')

    def update_job_applications_count(self):
        """Update total job applications count"""
        self.total_job_applications = self.job_applications.count()
        self.save()

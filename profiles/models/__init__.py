# profiles/models/__init__.py
from .base_profile import BaseProfile

from .jobseeker import (
    JobSeekerProfile,
    Education,
    WorkExperience,
    EXPERIENCE_CHOICES,
    EMPLOYMENT_STATUS,
    JOB_TYPE_CHOICES,
    WORK_ENVIRONMENT_CHOICES
)

__all__ = [
    'BaseProfile',
    'JobSeekerProfile',
    'Education',
    'WorkExperience',
    'EXPERIENCE_CHOICES',
    'EMPLOYMENT_STATUS',
    'JOB_TYPE_CHOICES',
    'WORK_ENVIRONMENT_CHOICES'
]

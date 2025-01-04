# profiles/models/jobseeker/choices.py
EXPERIENCE_CHOICES = (
    ('entry', 'Entry Level (0-2 years)'),
    ('junior', 'Junior Level (2-4 years)'),
    ('mid', 'Mid Level (4-6 years)'),
    ('senior', 'Senior Level (6-10 years)'),
    ('lead', 'Lead Level (10+ years)'),
)

EMPLOYMENT_STATUS = (
    ('actively_looking', 'Actively Looking'),
    ('employed_looking', 'Employed but Looking'),
    ('not_looking', 'Not Looking'),
    ('available_freelance', 'Available for Freelance')
)

JOB_TYPE_CHOICES = (
    ('full_time', 'Full Time'),
    ('part_time', 'Part Time'),
    ('contract', 'Contract'),
    ('freelance', 'Freelance'),
    ('remote', 'Remote'),
    ('internship', 'Internship')
)

WORK_ENVIRONMENT_CHOICES = (
    ('office', 'Office'),
    ('remote', 'Remote'),
    ('hybrid', 'Hybrid'),
)

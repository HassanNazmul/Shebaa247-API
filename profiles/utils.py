# profiles/models/jobseeker/utils.py
def calculate_completion_percentage(profile):
    required_fields = [
        'headline', 'summary', 'skills', 'experience_level', 'current_location', 'cv'
    ]
    optional_fields = [
        'languages', 'certifications', 'linkedin_profile', 'portfolio_link'
    ]

    total_fields = len(required_fields) + len(optional_fields)
    filled_fields = 0

    # Check required fields
    for field in required_fields:
        if getattr(profile, field):
            filled_fields += 1

    # Check optional fields
    for field in optional_fields:
        if getattr(profile, field):
            filled_fields += 1

    # Calculate percentage
    return int((filled_fields / total_fields) * 100)

# profiles/models/jobseeker/work_experience.py
from django.db import models

class WorkExperience(models.Model):
    profile = models.ForeignKey('JobSeekerProfile', on_delete=models.CASCADE, related_name='work_experiences')
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)
    responsibilities = models.TextField()
    achievements = models.TextField(blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.position} at {self.company}"

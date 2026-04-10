from django.db import models

# Create your models here.

class Bursary(models.Model):
    CATEGORY_CHOICES = [
        ('ALL', 'All'),
        ('ENG', 'Engineering'),
        ('EDU', 'Education'),
        ('MED', 'Medicine'),
        ('COM', 'Commerce'),
        ('LAW', 'Law'),
    ]
    category = models.CharField(
        max_length=3, 
        choices=CATEGORY_CHOICES, 
        default='ALL'
    )
    bursary_name = models.CharField(max_length=255)
    provider = models.CharField(max_length=255)
    summary = models.TextField()
    # Relationships
    # Many bursaries are only for specific Universities
    applicable_universities = models.ManyToManyField(
        'universities.University', 
        blank=True, 
        help_text="Leave blank if it applies to all universities"
    )
    
    # Many bursaries are only for specific fields (e.g. Engineering only)
    fields_of_study = models.CharField(
        max_length=255, 
        help_text="e.g. Engineering, Accounting, IT"
    )
    
    # Link to apply
    application_link = models.URLField()
    closing_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.bursary_name
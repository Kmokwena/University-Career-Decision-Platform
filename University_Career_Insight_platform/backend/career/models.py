from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class Career(models.Model):
    qualification = models.ManyToManyField(
        'qualification.Qualification',
        related_name='career')
    career_name = models.CharField(max_length=255)
    description = models.TextField()
    average_salary = models.DecimalField(max_digits=10, decimal_places=2,
                                         validators=[MinValueValidator(0)])
    industry = models.CharField(max_length=50, blank=True, null=True) # Feature will be implememnted in future

    def __str__(self):
        return self.career_name
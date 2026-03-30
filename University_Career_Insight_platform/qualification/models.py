from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Qualification(models.Model):
    university = models.ForeignKey(
        'universities.University', 
        on_delete=models.CASCADE, 
        related_name='qualifications')
    qualification_name = models.CharField(max_length=255)
    qualification_code = models.CharField(max_length=50)
    duration = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    field_of_study = models.CharField(max_length=255)
    NQF_level = models.PositiveSmallIntegerField(validators=[MinValueValidator(5), MaxValueValidator(10)])
    

    def __str__(self):
        return f'{self.qualification_name}'
    


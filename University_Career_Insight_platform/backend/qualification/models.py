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
        return self.qualification_name
    
class ThroughputStats(models.Model):
    qualification = models.OneToOneField(
        'Qualification', 
        on_delete=models.CASCADE, 
        related_name='stats'
    )
    
    # Can keep university if I want, but it's optional 
    # since qualification.university already exists.
    # university = models.ForeignKey(
    #     'universities.University', 
    #     on_delete=models.CASCADE
    # )

    cohort_year = models.PositiveIntegerField(help_text="The year this group of students started")
    total_intake = models.PositiveIntegerField(help_text="Total number of students who enrolled")
    graduated_n_plus_2 = models.PositiveIntegerField(help_text="Students who finished in N+2 years (CHE Standard)")
    
    # The 'Blocker Solver' Flag
    is_faculty_level = models.BooleanField(
        default=False, 
        help_text="Check this if data is for the whole Faculty (e.g., SET) rather than the specific degree."
    )
    
    @property
    def success_rate(self):
        if self.total_intake > 0:
            return round((self.graduated_n_plus_2 / self.total_intake) * 100, 2)
        return 0

    def __str__(self):
        return f"{self.university.university_name} - {self.qualification.qualification_name} Stats"

    class Meta:
        verbose_name_plural = "Throughput Stats"
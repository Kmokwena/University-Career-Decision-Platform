from django.db import models

# Create your models here.

class University(models.Model):
    university_name = models.CharField(max_length=255)
    university_code = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.university_name}'



class Location(models.Model):
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.city}, {self.province}'
    

class Campus(models.Model):
    university = models.ForeignKey(
        'universities.University',
        on_delete=models.CASCADE,
        related_name='campuses')
    location = models.ForeignKey(
        'universities.Location', 
        on_delete=models.CASCADE, 
        related_name='campuses')
    campus_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.campus_name} ({self.university})"
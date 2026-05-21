from rest_framework import serializers
from .models import University, Location, Campus

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['city', 'province']

class CampusSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)

    class Meta:
        model = Campus
        fields = ['campus_name', 'location']

class UniversitySerializer(serializers.ModelSerializer):
    campuses = CampusSerializer(many=True, read_only=True)

    class Meta:
        model = University
        fields = ['id', 'university_name', 'university_code', 'campuses']
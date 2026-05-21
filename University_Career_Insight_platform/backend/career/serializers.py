from rest_framework import serializers
from .models import Career
from qualification.serializers import QualificationSerializer

class CareerSerializer(serializers.ModelSerializer):
    qualification = QualificationSerializer(many=True, read_only=True)
    class Meta:
        model = Career
        fields = ['id', 'career_name', 'description', 'qualification']
from rest_framework import serializers
from .models import Bursary

class BursarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bursary
        # You can list specific fields, or use '__all__' to get everything
        fields = '__all__'
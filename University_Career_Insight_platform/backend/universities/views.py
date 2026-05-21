from django.shortcuts import render
from .models import University
from rest_framework import viewsets
from .serializers import UniversitySerializer
# Create your views here.
class UnviersityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
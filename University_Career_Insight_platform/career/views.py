from django.shortcuts import render
from .models import Career
from .serializers import CareerSerializer
from rest_framework import viewsets

# Create your views here.

class CareerViewSet(viewsets.ModelViewSet):
    queryset = Career.objects.all()
    serializer_class = CareerSerializer

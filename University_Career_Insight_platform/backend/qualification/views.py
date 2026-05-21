from django.shortcuts import render
from rest_framework import viewsets
from .serializers import QualificationSerializer
from .models import Qualification, ThroughputStats


# Create your views here.
class QualificationViewSet(viewsets.ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer
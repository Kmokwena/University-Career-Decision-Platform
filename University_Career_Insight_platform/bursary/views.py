from rest_framework import viewsets
from .models import Bursary
from .serializers import BursarySerializer

# Create your views here.

class BursaryViewSet(viewsets.ModelViewSet):
    queryset = Bursary.objects.all()
    serializer_class = BursarySerializer
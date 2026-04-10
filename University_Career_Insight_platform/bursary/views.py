from django.shortcuts import render
from .models import Bursary

# Create your views here.

def bursary_list(request):
    bursary = Bursary.objects.all()
    return render(request, 'bursary.html', {'bursary': bursary})

from django.shortcuts import render
from .models import University

# Create your views here.
def university_list(request):
    uni = University.objects.all()
    return render(request, 'universities/university.html', {'uni': uni})
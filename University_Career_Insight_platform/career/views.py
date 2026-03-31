from django.shortcuts import render

# Create your views here.

def career_list(request):
    return render(request, 'career.html')

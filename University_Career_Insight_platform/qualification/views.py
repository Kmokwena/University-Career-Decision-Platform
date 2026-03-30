from django.shortcuts import render


# Create your views here.
def qualification_list(request):
    return render(request, 'qualification.html')
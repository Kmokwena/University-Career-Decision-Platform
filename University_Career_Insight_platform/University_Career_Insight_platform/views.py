from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello, I am home!")

def about(request):
    return HttpResponse("Hello, I am about page.")
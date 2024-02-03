from django.shortcuts import HttpResponse

# Create your views here.

def app(request):
    return HttpResponse("Hello, Django FROM APP!")
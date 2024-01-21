from django.shortcuts import render

# Create your views here.

def homepage(request):
    #return HttpResponse("this is my homepage welcome to my home page")
    return render(request, "home.html")

def about(request):
    #return HttpResponse("this is my about page")
    return render(request, "about.html")
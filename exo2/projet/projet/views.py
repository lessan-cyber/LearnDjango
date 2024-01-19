from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'hero.html')

def layout(request):
    return render(request, 'layout.html')

def about(request):
    return render(request, 'about.html')
def popular(request):
    return render(request, 'popular.html')
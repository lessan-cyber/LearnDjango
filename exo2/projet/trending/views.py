from django.shortcuts import render

# Create your views here.

def trending(request):
    return render(request, 'trending/trending.html')

def subscription(request):
    return render(request, 'trending/subscription.html')
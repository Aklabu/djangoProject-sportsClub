from django.shortcuts import render

# Create your views here.
def football(request):
    return render(request, 'football.html')
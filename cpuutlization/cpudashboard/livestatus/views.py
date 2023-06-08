from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def live_status(request):
    
    return render(request, "live_status/live_status.html")

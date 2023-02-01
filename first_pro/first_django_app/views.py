from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def home(request):
    #date = datetime.datetime.now()
    #return HttpResponse("This is Index Page created on _ "+str(date))
    return render(request, "home.html", {})

def about(request):
    #return HttpResponse("This is About Page created on _ "+str(date))
    return render(request, "about.html", {})

def services(request):
    #return HttpResponse("This is About Page created on _ "+str(date))
    return render(request, "services.html", {})
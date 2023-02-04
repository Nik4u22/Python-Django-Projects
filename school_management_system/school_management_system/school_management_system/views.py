from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

def home_page(request):
    #date = datetime.datetime.now()
    #return HttpResponse("This is Index Page created on _ "+str(date))
    return render(request, "home.html", {})

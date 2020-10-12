from django.shortcuts import render
from .models import Destination
# Create your views here.
def about(request):
    return render(request,'travello/about.html',{})

def contact(request):
    return render(request,'travello/contactt.html',{})
    
def destinations(request):
    return render(request,'travello/destinations.html',{})
    
def elements(request):
    return render(request,'travello/elements.html',{})

def index(request):
    dests=Destination.objects.all()
    return render(request,'travello/index.html',{'dests':dests})
    
def news(request):
    return render(request,"travello/news.html",{})
    
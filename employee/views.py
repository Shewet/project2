from django.shortcuts import render

# Create your views here.
from .models import Person 
from .forms import PersonForm 
from django.http import HttpResponse  

  
def PersonView(request): 
    # dictionary for initial data with  
    # field names as keys 
    context={}    
    # add the dictionary during initialization 
    form = PersonForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
        return HttpResponse("Person is added in the system") 
    context['form']= form 
    return render(request, "employee/person.html", context) 
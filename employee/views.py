from django.shortcuts import render

# Create your views here.
from .models import Person 
from .forms import PersonForm 
from django.http import HttpResponse  

  
def PersonView(request): 
    # dictionary for initial data with  
    # field names as keys 
    context={}  
    if request.method == 'GET':
        context["dataset"] = Person.objects.all() 
        return  render(request, "employee/person_list.html", context)
    elif request.method == 'POST':
         
        # add the dictionary during initialization 
        form = PersonForm(request.POST or None) 
        if form.is_valid(): 
            form.save() 
            context['message']="Person Details Added to  the system"
            context["dataset"] = Person.objects.all() 
            return  render(request, "employee/person_list.html", context)
        context['form']= form 
        return render(request, "employee/person.html", context) 
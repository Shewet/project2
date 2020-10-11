from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from .models import Person 
from .forms import PersonForm 
from django.http import HttpResponse  

  
def PersonView(request): 
    # dictionary for initial data with  
    # field names as keys 
    context={}  
    context["dataset"] = Person.objects.all() 
    if not context["dataset"]:
        context['nullrecords'] = True
    else:
        context['nullrecords'] = False
    # if message:
    #     context['message']=message
    return  render(request, "employee/person_list.html", context)
 
 
def PersonCreate(request):
    
    context={}
    # add the dictionary during initialization 
    form = PersonForm(request.POST or None) 
    if form.is_valid(): 
        form.save() 
        context['message']="Person Details Added to  the system"
        return redirect(PersonView)
    context['form']= form 
    return render(request, "employee/person.html", context) 
    
    
def PersonUpdate(request,id):
    
    context={}
    obj = get_object_or_404(Person, id = id) 
    # add the dictionary during initialization 
    form = PersonForm(request.POST or None,instance=obj) 
    if form.is_valid(): 
        form.save() 
        context['message']="Person Details Added to  the system"
        return redirect(PersonView)
    context['form']= form 
    return render(request, "employee/person.html", context) 
    
    
    
def PersonDelete(request,id):
    
    context={}
    obj = get_object_or_404(Person, id = id) 
    if request.method == "POST":
        obj.delete()
        return redirect(PersonView) 
    context['data'] =obj    
    return render(request, "employee/person_delete.html", context) 
     
     
     
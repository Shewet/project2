from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def home(request):
#     return HttpResponse("Hello World")
    
def home(request):
    return render(request,'calc/index.html',{"name":"Sheweta"})
    
def add(request):
    val1=request.POST['num1']
    val2=request.POST['num2']
    result=int(val1)+int(val2)
    return render(request,'calc/result.html',{"num1":val1,"num2":val2,"result":result})
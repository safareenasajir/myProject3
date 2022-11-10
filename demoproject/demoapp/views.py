from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import task

# Create your views here.
def demo(request):
     obj=place.objects.all()
     return render(request,'index.html',{'result':obj})

def demo1(request):
    obj1=task.objects.all()
    return render(request,'index.html',{'result':obj1})
#def addition(request):
 #   x=int(request.GET['num1'])
  #  y=int(request.GET['num2'])
   # res=x+y
    #return render(request,"result.html",{'result':res})
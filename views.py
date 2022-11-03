from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
##
# Create your views here.
'''#def a(request):
	#b=c(name="Flksx",address="Pune",empID=79)
	#b.save()
	#x=c()
	#x.name="fgj"
	#x.address="atp"
	#x.empID=90
	#x.save()
	#return HttpResponse("Django")
	#return render(request,"n.html",context={})
def func(request):
    #return render(request,"page1.html",context={})
    if request.method=='POST':
       name=request.POST.get("nm")
       address=request.POST.get("add")
       city=request.POST.get("city")
       pincode=request.POST.get("pin")
    print(name,address,city,pincode)
    return HttpResponse("Check console")
    #return redirect("page2")

def func2(request):
    #ab=c.objects.get(empID=75020)
    #ab=c.objects.filter(empID=75020)
    #ab=c.objects.all()
    #print(ab)
    #print(ab.name,ab.address,ab.empID)
    #return render(request,"page1.html",context={'name':'Veda'})
    return render(request,"page1.html",context={})
'''

def f(request):
    if request.method=='POST':
       name=request.POST.get("name")
       address=request.POST.get("add")
       empID=request.POST.get("empID")
       print(name,address,empID)
       a1=c(name=name,address=address,empID=empID)   
       a1.save()
       print(name,address,empID)
    else:
        return render(request,"h.html",context={})
    return HttpResponse("Check console")


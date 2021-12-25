from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request.POST)
<<<<<<< HEAD
    form={'form':"Product Name         <input name='Productname' type='text'> "}
    return render(request,"index.html",form)
=======
    return render(request,"generatebill.html")

def addformfield(request):
    formcount=request.formcount
    while formcount<8:
        pass

    return render(request,"generatebill.html")
    pass
>>>>>>> 4d7bcd29961ffff2c1323077ba86397f1f846d10

def addformfield(request):
    formcount=request.formcount
    while formcount<8:
        pass

    return render(request,"index.html")
    

def check(request):
    return render(request,"hi.html")
    
# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request.POST)

    form={'form':"Product Name         <input name='Productname' type='text'> "}
    return render(request,"index.html",form)

    

def addformfield(request):
    formcount=request.formcount
    while formcount<8:
        pass

    return render(request,"generatebill.html")



def addformfield(request):
    formcount=request.formcount
    while formcount<8:
     pass


    return render(request,"index.html")


# Create your views here.

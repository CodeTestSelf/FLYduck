from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request.POST)
    return render(request,"generatebill.html")

def addformfield(request):
    formcount=request.formcount
    while formcount<8:
        pass

    return render(request,"generatebill.html")
    pass

# Create your views here.

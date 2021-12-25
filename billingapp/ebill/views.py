from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    print(request.POST)
    return render(request,"index.html")


# Create your views here.

from django.shortcuts import render

def index(request):
    return render(request,"hi.html")

# Create your views here.

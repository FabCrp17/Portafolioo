from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def SobreMi(request):
    return render(request, 'sobre_mi.html')

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index_europa(resquest):
    return render(resquest, 'europa.html')

def italia(request):
    return render(request, 'franca.html')

def franca(request):
    return render(request, 'franca.html')

def alemanha(request):
    return render(request, 'alemanha.html')
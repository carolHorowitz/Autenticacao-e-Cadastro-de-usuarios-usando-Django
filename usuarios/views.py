from django.shortcuts import render

from .models import Usuario

def cadastro(request):
    return render(request, 'cadastro.html')

def login(request):
    return render(request, 'login.html')    
   



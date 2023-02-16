from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required

def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.filter(username=username).first()
        
        if user:
            return HttpResponse("Já existe um usuário cadastrado com esse username.")
        
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        user.save()
        
        return HttpResponse("Usuário cadastrado com sucesso")
        

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    
    else: 
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            login_django(request, user)
            
            return HttpResponse("Autenticado")
        else:
            return HttpResponse("Usuário ou Senha inválidos") 
        
@login_required(login_url="/usuarios/login/")
def plataforma(request):
    return HttpResponse("Plataforma")
    



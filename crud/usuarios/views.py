from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bem vindo ao painel de cadastro do usuários")



from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

def index(request):
    name_list = Usuario.objects.all()
    return HttpResponse(name_list)

   



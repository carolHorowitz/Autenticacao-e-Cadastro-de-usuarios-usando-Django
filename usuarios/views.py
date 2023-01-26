from django.shortcuts import render

from .models import Usuario

def index(request):
    name_list = Usuario.objects.all()
    context = {'name_list': name_list,}
    return render(request, 'usuarios/index.html', context)

   



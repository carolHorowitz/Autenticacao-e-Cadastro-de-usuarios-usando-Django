from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    telefone = models.CharField(max_length=10, null=False, blank=False)
    email = models.CharField(max_length=30, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    data_nascimento = models.CharField(max_length=10, null=False, blank=False)
    





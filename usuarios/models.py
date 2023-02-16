from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=30, null=False, blank=False)
    password = models.CharField(max_length=11, null=False, blank=False)
    





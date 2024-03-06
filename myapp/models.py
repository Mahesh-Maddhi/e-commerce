from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser, BaseUserManager

class SignedUser(models.Model):

    username = models.CharField(max_length = 100,primary_key = True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length = 200)
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.username
    

class Contact(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=200)
    date = models.DateField(default = datetime.now)

    def __str__(self):
        return self.firstname + " "+ self.lastname

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
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    user_message = models.TextField()
    date = models.DateField(default = datetime.now)

    def __str__(self):
        return self.full_name

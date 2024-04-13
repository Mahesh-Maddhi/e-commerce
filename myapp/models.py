from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    user_message = models.TextField()
    date = models.DateField(default = datetime.now)

    def __str__(self):
        return self.full_name


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE)
    product_id = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.username) + " " + self.title
    
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discountPercentage = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.FloatField()
    stock = models.PositiveIntegerField()
    brand = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=255)
    images = models.JSONField()

    def __str__(self):
        return self.brand + " " + self.title 
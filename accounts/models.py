from django.db import models

# Create your models here.

class patient(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    uname = models.CharField(max_length=30)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length=20)

# class doctor(models.Model):
#     fname = models.CharField(max_length=30)
#     lname = models.CharField(max_length=30)
#     uname = models.CharField(max_length=30)
#     email = models.EmailField(max_length = 254)
#     password = models.CharField(max_length=30, min_length=8)

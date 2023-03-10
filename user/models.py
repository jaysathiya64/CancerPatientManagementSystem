from django.db import models

# Create your models here.
class Usersignup(models.Model):
    id= models.AutoField(primary_key=True)
    fname= models.CharField(max_length=15)
    lname= models.CharField(max_length=15)
    uname= models.CharField(max_length=15)
    email= models.EmailField(max_length=20)
    password= models.CharField(max_length=15)

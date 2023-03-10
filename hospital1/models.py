from django.db import models

# Create your models here.
class Registerdetail(models.Model):
    h_id= models.AutoField(primary_key=True)
    h_name= models.CharField(max_length=35)
    h_email= models.EmailField(max_length=20)
    h_pwd= models.CharField(max_length=15)
    h_address= models.CharField(max_length=50)
    h_pincode= models.IntegerField()

class Doctordetail(models.Model):
    d_id= models.AutoField(primary_key=True)
    d_name= models.CharField(max_length=20)
    d_email= models.EmailField(max_length=20)
    d_pwd= models.CharField(max_length=15)
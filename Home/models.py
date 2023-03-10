from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.

class suggest_hospital(models.Model):
    cancer_type = models.CharField(max_length=30)
    hospital_name = models.CharField(max_length=30)

class Item(models.Model):
    video = EmbedVideoField()

class Physio(models.Model):
    video = EmbedVideoField()

class Feedback(models.Model):
    uname = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    note = models.CharField(max_length=200)

class Book(models.Model):
    ap_id= models.AutoField(primary_key=True)
    ap_patient_fname= models.CharField(max_length=15)
    ap_patient_lname= models.CharField(max_length=15)
    ap_patient_email= models.EmailField(max_length=30)
    ap_patient_number= models.CharField(max_length=10)
    cancer_type= models.CharField(max_length=15)
    ap_time= models.DateTimeField()
    ap_label= models.TextField()    
    ap_doc_fname= models.CharField(max_length=15)
    ap_doc_lname= models.CharField(max_length=15)
    
class Hospital(models.Model):
    h_id= models.AutoField(primary_key=True)
    h_name= models.CharField(max_length=35)
    h_email= models.EmailField(max_length=20)
    h_pwd= models.CharField(max_length=15)
    h_address= models.CharField(max_length=50)
    h_pincode= models.IntegerField()

class Doctors(models.Model):
    d_id= models.AutoField(primary_key=True)
    d_fname= models.CharField(max_length=20)
    d_lname= models.CharField(max_length=20)
    d_email= models.EmailField(max_length=20)
    d_pwd= models.CharField(max_length=15)
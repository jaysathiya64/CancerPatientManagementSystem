from django.db import models

# Create your models here.

class Book(models.Model):
    ap_id= models.AutoField(primary_key=True)
    ap_patient_fname= models.CharField(max_length=15)
    ap_patient_lname= models.CharField(max_length=15)
    ap_patient_email= models.EmailField(max_length=20)
    ap_patient_number= models.CharField(max_length=10)
    cancer_type= models.CharField(max_length=15)
    ap_time= models.DateTimeField()
    h_name= models.CharField(max_length=20)
    d_name= models.CharField(max_length=20)

class Feedback(models.Model):
    f_id=models.AutoField(primary_key=True)
    p_fname=models.CharField(max_length=15)
    p_lname=models.CharField(max_length=15)
    p_email= models.EmailField(max_length=20)
    ap_label= models.TextField()


from django.shortcuts import render, redirect
from django.contrib import messages
import datetime
from django.contrib.auth.models import User, auth
from .models import suggest_hospital
from .models import Item
from .models import Physio
from .models import Feedback
from .models import Book
from .models import Hospital
from .models import Doctors
from accounts.models import patient

# Create your views here.
def index(request):
    obj = Item.objects.all()
    return render(request, 'index.html', {'obj' : obj})
    
def diet(request):
    return render(request, 'diet.html')

def physio(request):
    obj = Physio.objects.all()
    return render(request, 'physio.html' ,{'obj' : obj})

def payment(request):
    return render(request, 'payment.html')

def back(request):
    return render(request, 'index.html')

def userfeedback(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        email = request.POST['email']
        fb = request.POST['fb']

        if request.session['uname']:
                uname = request.session['uname']
        allpatient = patient.objects.filter(uname=uname)
        context = {"patientobj":allpatient}


        valid= patient.objects.filter(uname=uname, email=email)
        if valid:
            Feedback(uname=uname, email=email, note=fb).save()
            messages.info(request,"Your feedback is submitted successfully")
            return render(request, 'index.html')
        else:
            return render(request,'feedback.html')        
    else:
        if request.session['uname']:
                uname = request.session['uname']
        allpatient = patient.objects.filter(uname=uname)
        context={"patientobj":allpatient}
        return render(request, 'feedback.html',context)

def bookapp(request):
    if request.method == 'POST':
        ap_patient_fname = request.POST['ap_patient_fname']
        ap_patient_lname = request.POST['ap_patient_lname']
        ap_patient_email = request.POST['ap_patient_email']
        ap_patient_number = request.POST['ap_patient_number']
        cancer_type= request.POST['cancer_type']
        ap_time = request.POST['ap_time']
        ap_label = request.POST['ap_label']
        ap_doc_fname = request.POST['ap_doc_fname']
        ap_doc_lname = request.POST['ap_doc_lname']

        if request.session['uname']:
            uname = request.session['uname']
        allpatient = patient.objects.filter(uname=uname)
        context={"patientobj":allpatient}

        if Book.objects.filter(ap_time=ap_time,ap_doc_fname=ap_doc_fname).exists():
            messages.info(request,'One appointment already booked with given time, So you have to change the time of your appointment or change the doctor.')
            return render(request,'appointment.html', context)
        else:
            valid = patient.objects.filter(email=ap_patient_email)
            if valid:
                appointment=Book(ap_patient_fname=ap_patient_fname,
                    ap_patient_lname=ap_patient_lname,
                    ap_patient_email=ap_patient_email,
                    ap_patient_number=ap_patient_number,
                    cancer_type=cancer_type,
                    ap_time=ap_time,
                    ap_label=ap_label,
                    ap_doc_fname=ap_doc_fname,
                    ap_doc_lname=ap_doc_lname
                )
                appointment.save()
                book=Book.objects.latest('ap_id')
                return render(request, 'submitted_appointment.html', {'book': book})
            else:
                messages.info(request, "Check your email and try again.")
                return render(request,'appointment.html', context)
    else:
        if request.session['uname']:
            uname = request.session['uname']
        allpatient = patient.objects.filter(uname=uname)
        context={"patientobj":allpatient}
        return render(request,'appointment.html', context)
    
def seeapp(request):    
    if request.session['uname']:
        uname = request.session['uname']
        allpatient = patient.objects.filter(uname=uname)
        for p in allpatient:
            email = p.email            
        allbook=Book.objects.filter(ap_patient_email=email)
        context={"bookappointment":allbook}
        return render(request, 'seeapp.html', context)
    else:
        messages.info(request, "appointment session not started..")    

def deleteapp(request, ap_id):
    cancel = Book.objects.get(ap_id=ap_id)
    cancel.delete()
    return render(request, 'seeapp.html')

def hospital_login(request):
    if request.method == 'POST':
        h_name= request.POST['h_name']
        h_email= request.POST['h_email']
        h_pwd= request.POST['h_pwd']
        h_address= request.POST['h_address']
        h_pincode= request.POST['h_pincode']
        hospital=Hospital(h_name=h_name,
            h_email=h_email,h_pwd=h_pwd,h_address=h_address,h_pincode=h_pincode
        )
        hospital.save()
        return render(request,'hlogin.html')
    else:
        return render(request, 'Register_hospital.html')

def hospital_home(request):
    return render(request,'hospital_home.html')
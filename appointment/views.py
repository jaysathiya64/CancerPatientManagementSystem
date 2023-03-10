from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from appointment.models import Book
from user.models import Usersignup
from appointment.models import Feedback
from django.contrib import messages
# Create your views here.

def bookap(request):
    if request.method == 'POST':
        ap_patient_fname = request.POST['ap_patient_fname']
        ap_patient_lname = request.POST['ap_patient_lname']
        ap_patient_email = request.POST['ap_patient_email']
        ap_patient_number = request.POST['ap_patient_number']
        cancertype= request.POST['cancertype']
        ap_time = request.POST['ap_time']
        h_name = request.POST['hospitals']
        d_name = request.POST['doctors']
            
        if Book.objects.filter(ap_time=ap_time).exists():
            messages.info(request,'Select Different Time Slot')
            return render(request,'appointment.html')
        else:
            appointment=Book(ap_patient_fname=ap_patient_fname,
                ap_patient_lname=ap_patient_lname,
                ap_patient_email=ap_patient_email,
                ap_patient_number=ap_patient_number,
                cancer_type=cancertype,
                ap_time=ap_time,
                h_name=h_name,
                d_name=d_name
            )
            appointment.save()
            book=Book.objects.latest('ap_id')
            request.session['p_email']=request.POST['ap_patient_email']
            return render(request,'bookap.html',{'book':book})
    else:
        return render(request,'appointment.html')
            
def seeappointment(request):
    email=request.session.get('p_email')
    if  Book.objects.filter(ap_patient_email=email).exists():
        allap=Book.objects.all()
        Data={"bookap":allap}
        return render(request,'seeappointment.html',Data)
    else:
        messages.info(request,'Not any appointment booked with doctor')
        return render(request,'seeappointment.html')

def sfeedback(request):
    if request.method == 'POST':
        p_fname = request.POST['p_fname']
        p_lname = request.POST['p_lname']
        ap_label = request.POST['ap_label']
        feedback=Feedback(p_fname=p_fname,
            p_lname=p_lname,
            ap_label=ap_label
        )
        feedback.save()
        messages.info(request,'Feedback submitted successfully')
        return render(request,'feedback.html')
    else:
        return render(request,'feedback.html')




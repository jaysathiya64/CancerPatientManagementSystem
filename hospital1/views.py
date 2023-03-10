from django.shortcuts import render,redirect
from django.contrib import messages
from hospital1.models import Registerdetail
from appointment.models import Book
from hospital1.models import Doctordetail
# Create your views here.
def hlogin(request):
    if request.method == 'POST':
        h_name=request.POST['h_name']
        h_pwd=request.POST['pwd']
        
        if Registerdetail.objects.filter(h_name=h_name).exists():
            if Registerdetail.objects.filter(h_pwd=h_pwd).exists():

                allbook=Book.objects.filter(h_name=h_name)
                Context={"bookappointment":allbook}
                return render(request,'mainhome.html',Context)
                
            else:
                messages.error(request,'Wrong username or password')
                return render(request,'login.html')
        else:
            messages.info(request,'Please register your hospital first using click an above link')
            return render(request,'login.html')
    else:
        return render(request,'login.html')

def hsignup(request):
    if request.method == 'POST':
        h_name= request.POST['h_name']
        h_email= request.POST['h_email']
        h_pwd= request.POST['h_pwd']
        h_address= request.POST['h_address']
        h_pincode= request.POST['h_pincode']
        register=Registerdetail(h_name=h_name,
            h_email=h_email,h_pwd=h_pwd,h_address=h_address,h_pincode=h_pincode
        )
        register.save()
        return render(request,'login.html')
    else:
        return render(request,'signup.html')

def signup(request):
    return render(request,'signup.html')

def adddoctor(request):
    if request.method == 'POST':
        dname= request.POST['dname']
        demail= request.POST['demail']
        dpwd= request.POST['dpwd']
        if Doctordetail.objects.filter(d_email=demail).exists():
            messages.info(request,'Doctor already registerd')
            return render(request,'adddoctor.html')
        else:
            doctor=Doctordetail(d_name=dname,d_email=demail,d_pwd=dpwd)
            doctor.save()
            messages.success(request,'Doctor added successfully')
            allbook=Book.objects.all()
            Context={"bookappointment":allbook}
            return render(request,'mainhome.html',Context)        
    else:
        return render(request,'adddoctor.html')
def doctorlogin(request):
    if request.method == 'POST':
        login_email=request.POST['login_email']
        login_pwd=request.POST['login_pwd']

        if Doctordetail.objects.filter(d_email=login_email).exists():
            if Doctordetail.objects.filter(d_pwd=login_pwd).exists():
                return render(request,'doctorhome.html')
            else:
                return render(request,'doctorlogin.html')
        else:
            messages.info(request,'Please register yourself through the hospital ')
            return render(request,'dlogin.html')
    else:
        return render(request,'doctorlogin.html')


def home(request):
    allbook=Book.objects.all()
    Context={"bookappointment":allbook}
    return render(request,'mainhome.html',Context)

def registerdoctor(request):
    doctor=Doctordetail.objects.all()
    return render(request,'registerdoctor.html',{'alldoctor':doctor})

def remove(request,d_id):
    remove=Doctordetail.objects.get(d_id=d_id)
    remove.delete()
    return redirect("registerdoctor")

def cancel(request,ap_id):
    cancel=Book.objects.get(ap_id=ap_id)
    cancel.delete()
    return redirect("/mainhome")

def cancelap(request,ap_id):
    cancel=Book.objects.get(ap_id=ap_id)
    cancel.delete()
    return redirect("/seeappointment")

def hlogout(request):
    return redirect("/hlogin")

def dlogout(request):
    return redirect("/doctorlogin")

    
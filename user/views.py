from django.shortcuts import render,redirect   
from django.contrib import messages
from user.models import Usersignup

# Create your views here.
def ulogin(request):
    if request.method == 'POST':
        email=request.POST['email']
        pwd=request.POST['pwd']

        if Usersignup.objects.filter(email=email).exists():
            # if Usersignup.objects.filter(password=pwd).exists():
            return render(request,'appointment.html')
            # else:
            #     return render(request,'ulogin.html')
        else:
            messages.info(request,'Please register yourself')
            return render(request,'ulogin.html')
    else:
        return render(request,'ulogin.html')

    return render(request,'ulogin.html')

def usignup(request):
    
    if request.method == 'POST':
        fname= request.POST['fname']
        lname= request.POST['lname']
        uname= request.POST['uname']
        email= request.POST['email']
        password= request.POST['pwd']
        
        if Usersignup.objects.filter(uname=uname).exists():
            messages.error(request,'User already exist')
            return render(request,'ulogin.html')
        else:   
            userdetails=Usersignup(fname=fname,lname=lname,uname=uname,email=email,password=password)
            userdetails.save()
            request.session['fname']= request.POST['fname']
            request.session['lname']= request.POST['lname']
            request.session['email']= request.POST['email']
            return render(request,'ulogin.html')
    else:
        return render(request,'usignup.html')

def userlogin(request):
    if request.method == 'POST':
        email=request.POST['email']
        pwd=request.POST['pwd']

        if Usersignup.objects.filter(email=email).exists():
            # if Usersignup.objects.filter(password=pwd).exists():
            return render(request,'appointment.html')
            # else:
            #     return render(request,'ulogin.html')
        else:
            messages.info(request,'Please register yourself')
            return render(request,'ulogin.html')
    else:
        return render(request,'ulogin.html')

def usersignup(request):
    return render(request,'usignup.html')

def ulogout(request):
    return redirect("/ulogin.html")
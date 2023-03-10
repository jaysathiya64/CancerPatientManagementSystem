from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import patient
# Create your views here.

def register(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        uname = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
      #  password2 = request.POST['password2']
        f = 0
        
        patients = patient.objects.all()
        for p in patients:
            if p.uname == uname:
                f = 1
                messages.info(request, "Username is already taken. Please enter another username.")
                break
            if p.email == email:
                f = 1
                messages.info(request, "Email is already taken. Please enter another email.")
                break
        if f == 0:
            patient(fname=fname, lname=lname, uname=uname, email=email, password=password1).save()
            messages.info(request, " Hello, " + request.POST['username'] + ". You have registered successfully.")
            request.session['uname'] = uname
            return render(request,'index.html')
            #return render(request, 'login.html')
        else:
            return render(request, 'register.html')
    else:
        return render(request , 'register.html')     

def login(request):
    if request.method == 'POST':
        try:
            userdetails = patient.objects.get(uname=request.POST['uname'],email=request.POST['email'], password=request.POST['password'])
            request.session['uname'] = userdetails.uname
            return render(request,'index.html')
        except patient.DoesNotExist as e:
            messages.info(request,"Email / Password does not match...")
    return render(request, 'login.html')

def logout(request):
    try:
        del request.session['uname']
    except:
        return render(request, 'index.html')
    return render(request, 'login.html') 
    
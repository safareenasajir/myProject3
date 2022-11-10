from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return  redirect('/')
            else:
                messages.info(request, "invalid credential")
                return redirect('login')



    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')
def register(request):
    if request.method=='POST':
        uname=request.POST['username']
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        email=request.POST['email']
        passwrd=request.POST['password1']
        cpasswrd=request.POST['password2']
        if passwrd==cpasswrd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,"username exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email exist")
                return redirect('register')
            else:

              user=User.objects.create_user(username=uname,password=passwrd,first_name=fname,last_name=lname,email=email)
              user.save()
              return redirect('login')

            # return redirect('/')
        else:
            messages.info(request,"password not match")
            return redirect('register')
    return render(request,'register.html')
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate
from .models import Customer
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobileno= request.POST['mobno']
        village= request.POST['vil']
        password1= request.POST['Password1']
        password2= request.POST['Password2']
        values=[name,mobileno]
        if password1 == password2:
            if Customer.objects.filter(name = name).exists():
               messages.info(request,"***Username exists***")
            else:
                user = User.objects.create_user(
                    username=name,
                    email=mobileno,
                    last_name=village,
                    password=password1                          
                )
                
                messages.info(request,"*** Registered Succesfully ***")
                user.save()
               
            return render(request,'register.html',{'username':values})
            print("reached home succesfully through post")
        else:
             messages.info(request,"***Passwords not matched***")
             return render(request,'register.html',{'username':values})
            
             
    else:
        return render(request,'register.html')



def registercust(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobileno= request.POST['mobno']
        village= request.POST['vil']
        password1= request.POST['Password1']
        password2= request.POST['Password2']
        values=[name,mobileno]
        if password1 == password2:
            if Customer.objects.filter(name = name).exists():
               messages.info(request,"***Username exists***")
            else:
                user = Customer.objects.create(
                    name=name,
                    mobileno=mobileno,
                    village=village,
                    password=password1                          
                )
                
                messages.info(request,"*** Registered Succesfully ***")
                user.save()
               
            return render(request,'register.html',{'username':values})
            print("reached home succesfully through post")
        else:
             messages.info(request,"***Passwords not matched***")
             return render(request,'register.html',{'username':values})
            
             
    else:
        return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password1= request.POST['Password1']
        user = auth.authenticate(username=name,password=password1)
        if user is not None:
            auth.login(request,user)
            return redirect('/loggedin')
        else:
            messages.info(request,"***Invalid credentials***")
            return redirect('login')
       
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
  
def loggedin(request):
    return render(request,'loggedin.html')